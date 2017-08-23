from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^day/$', views.DayListView.as_view(), name='show_self'),
	url(r'^day/(?P<day>[\w\-]+)/$', views.DayDetailView.as_view(), name='day_detail'),
	url(r'^$', views.ProgramListView.as_view(), name= 'program_detail'),
	url(r'^P-(?P<slug>[\w\-]+)/$', views.ProgramDetailView.as_view(), name='program_detail'),
]
