from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    #'http://127.0.0.1:8000/' 주소일 때 views.post_list
]