from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_list', views.post_list, name='post_list' ),
    path('post_create', views.post_create, name="post_create"),
]
