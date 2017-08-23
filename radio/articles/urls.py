from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'tag/(?P<tag_name>.+)/$', views.TagDetailView.as_view(), name='tag_detail'),
    url(r'create/$', views.ArticleCreateView.as_view(), name='create_article'),
    url(r'list/$', views.ArticleListView.as_view(), name='article_list'),
    url(r'drafts/$', views.DraftArticlesListView.as_view(), name='draft_article'),
    url(r'A-(?P<slug>[-\w]+)/$', views.ArticleDetailView.as_view(), name='article_detail'),
    url(r'^comment/$', views.comment, name='comment'),
    # url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit_article'),
]