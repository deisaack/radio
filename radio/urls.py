from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import radio.profiles.urls
import radio.accounts.urls
import radio.programs.urls
import radio.articles.urls
from . import views
from ckeditor_uploader import views as ck_views

urlpatterns = [
    url(r'^article/', include(radio.articles.urls, namespace='articles')),
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^', include(radio.accounts.urls, namespace='accounts')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(radio.profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^program/', include(radio.programs.urls, namespace='program')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^ckeditor/browse/', ck_views.browse, name='ckeditor_browse'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
