from django.urls import path

from posts import views
# from posts.views import post_list, post_detail

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('<int:pk>/', views.post_detail, name='post-detail'),
]
