from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', include('config.urls.views')),
    path('api/', include('config.urls.apis'))
]