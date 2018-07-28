from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
        path('posts/', include('posts.urls.apis')),
        path('users/', include('members.urls.apis')),
]
urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)


# a += 1
# a = a+1