from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from members.apis import UserList
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls.views')),
    path('', views.index, name='index'),
    path('members/', include('members.urls.views')),
    path('api/', include([
        path('posts/', include('posts.urls.apis')),
        path('users/', include('members.urls.apis')),
    ])),
] + static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
