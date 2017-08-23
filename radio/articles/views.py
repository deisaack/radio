from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from .forms import ArticleForm
from .models import Article, ArticleComment, Tag
from django.views.generic import DetailView, CreateView, ListView, View
from django.urls import reverse
from django.conf import settings

User = settings.AUTH_USER_MODEL


class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.all().filter(status=Article.PUBLISHED)


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm

    def get_success_url(self):
        return reverse('articles:article_detail', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        tags = form.cleaned_data.get('tags')
        self.object.save()
        article = self.object.pk
        Article.create_tags(article, tags)
        return super(ArticleCreateView, self).form_valid(form)


class DraftArticlesListView(ListView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super(DraftArticlesListView, self).get_context_data(**kwargs)
        if self.request.user.is_superuser:
            context['article_list'] = Article.objects.all().filter(status=Article.DRAFT)
        else:
            context['article_list'] = Article.objects.all().filter(status=Article.DRAFT, creator=self.request.user)
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all().filter(article__slug=self.kwargs['slug'])
        return context

class TagDetailView(View):
    def get(self, request, tag_name):
        articles = Article.objects.all().filter(tag__name=tag_name, status=Article.PUBLISHED)
        return render(request, 'articles/article_list.html', {'article_list': articles})


def comment(request):
    try:
        if request.method == 'POST':
            article_id = request.POST.get('article')
            article = Article.objects.get(pk=article_id)
            comment = request.POST.get('comment')
            comment = comment.strip()
            if len(comment) > 0:
                article_comment = ArticleComment(user=request.user,
                                                 article=article,
                                                 comment=comment)
                article_comment.save()
            html = ''
            for comment in article.get_comments():
                html = '{0}{1}'.format(html, render_to_string(
                    'articles/partial_article_comment.html',
                    {'comment': comment}))

            return HttpResponse(html)

        else:
            return HttpResponseBadRequest()

    except Exception:
        return HttpResponseBadRequest()



# @login_required
# def edit(request, id):
#     tags = ''
#     if id:
#         article = get_object_or_404(Article, pk=id)
#         for tag in article.get_tags():
#             tags = '{0} {1}'.format(tags, tag.name)
#         tags = tags.strip()
#     else:
#         article = Article(creator=request.user)
#
#     if article.creator.id != request.user.id:
#         return redirect('home')
#
#     if request.POST:
#         form = ArticleForm(request.POST, instance=article)
#         if form.is_valid():
#             form.save()
#             return redirect('/articles/')
#     else:
#         form = ArticleForm(instance=article, initial={'tags': tags})
#     return render(request, 'articles/edit.html', {'form': form})
#
