from django.urls import path

from . import views
# from posts.views import post_list, post_detail

app_name = 'posts'
urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('<int:pk>/', views.post_detail, name='post-detail'),
    # path('posts', views.index),
    path('create/', views.post_create, name='post-create'),
    path('delete/<int:pk>', views.post_delete, name='post-delete'),
]
