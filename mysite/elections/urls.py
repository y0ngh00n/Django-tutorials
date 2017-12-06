from django.conf.urls import url
#from django.contrib import admin
from . import views # .은 현재 폴더

app_name = 'elections'
urlpatterns = [
	url(r'^$', views.index, name = 'home'),
    url(r'^$', views.index), # 그냥 localhost8000가 넘어오면 views.index를 내보내라.
    url(r'^areas/(?P<area>[가-힣]+)/$', views.areas),
    url(r'^areas/(?P<area>[가-힣]+)/results$', views.results),
    url(r'^polls/(?P<poll_id>\d+)/$', views.polls),
    url(r'^candidates/(?P<name>[가-힣]+)/$', views.candidates),
]