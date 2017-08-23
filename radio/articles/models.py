from datetime import datetime
from django.conf import  settings
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class ArticleManager(models.Manager):
    def all(self, *args, **kwargs):
        return super(ArticleManager, self).all().filter(publish__lte =timezone.now().date())


class Article(models.Model):
    DRAFT = 'D'
    PUBLISHED = 'P'
    STATUS = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(editable=False, unique=True)
    content = RichTextUploadingField(max_length=10000)
    status = models.CharField(max_length=1, choices=STATUS, default=DRAFT)
    creator = models.ForeignKey(User, null=True, blank=True)
    publish = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    updator = models.ForeignKey(User, null=True, blank=True, related_name="+")

    objects = ArticleManager()

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ("-created",)

    def get_absolute_url(self):
        return reverse('articles:article_detail', kwargs={'slug':self.slug})

    def __str__(self):
        return self.title


    def create_slug(instance, x=2, new_slug=None,):
        slug = slugify(instance.title)
        if new_slug is not None:
            slug = new_slug
        qs = Article.objects.filter(slug=slug).order_by('-id')
        exists = qs.exists()
        if exists:
            slug = '%s-%s' % (slugify(instance.title), x)
            x += 1
            return Article.create_slug(instance, x=x, new_slug=slug)
        return slug

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = Article.create_slug(self)
            super(Article, self).save(*args, **kwargs)
        else:
            self.updated = datetime.now()
        if not self.slug:
            self.slug = Article.create_slug(self)


        super(Article, self).save(*args, **kwargs)

    @staticmethod
    def get_published():
        articles = Article.objects.filter(status=Article.PUBLISHED)
        return articles

    def create_tags(self, tags):
        tags = tags.strip()
        tag_list = tags.split(' ')
        for tag in tag_list:
            if tag:
                Tag.objects.get_or_create(tag=tag.lower(), article_id = self)

    def get_tags(self):
        return Tag.objects.filter(article=self)

    def get_summary(self):
        if len(self.content) > 255:
            return '{0}...'.format(self.content[:255])
        else:
            return self.content

    def get_comments(self):
        return ArticleComment.objects.filter(article=self)

admin.site.register(Article)


class Tag(models.Model):
    name = models.CharField(max_length=50)
    article = models.ForeignKey(Article)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')
        unique_together = (('name', 'article'),)
        index_together = [['name', 'article'], ]

    def __str__(self):
        return self.tag

    def create_tags(self, tags):
        tags = tags.strip()
        tag_list = tags.split(' ')
        for tag in tag_list:
            if tag:

                t, created = Tag.objects.get_or_create(tag=tag.lower(),
                                                       article_id = self)


    @staticmethod
    def get_popular_tags():
        tags = Tag.objects.all()
        count = {}
        for tag in tags:
            if tag.article.status == Article.PUBLISHED:
                if tag.name in count:
                    count[tag.name] = count[tag.name] + 1
                else:
                    count[tag.name] = 1
        sorted_count = sorted(count.items(), key=lambda t: t[1], reverse=True)
        return sorted_count[:20]

admin.site.register(Tag)

class ArticleComment(models.Model):
    article = models.ForeignKey(Article)
    comment = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = _("Article Comment")
        verbose_name_plural = _("Article Comments")
        ordering = ("date",)

    def __str__(self):
        return '{0} - {1}'.format(self.user.username, self.article.title)

admin.site.register(ArticleComment)
