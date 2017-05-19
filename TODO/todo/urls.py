from django.conf.urls import url
from todo import views

urlpatterns = [
    url(r'^todo/$', views.TodoList.as_view()),
    url(r'^todo/(?P<pk>[0-9]+)/$', views.TodoDetail.as_view()),
]