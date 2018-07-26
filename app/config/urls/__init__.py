from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from members.apis import UserList
from .. import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls.posts')),
    path('', views.index, name='index'),
    path('members/', include('members.urls')),
    path('api/<str:api_type>/', views.link_api, name='api'),

    path('api/', include('posts.urls.apis')),
    # path('members/', include('members.urls')),
] + static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
