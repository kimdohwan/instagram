from django.urls import path

from .. import apis

# app_name = 'apis'
urlpatterns = [
    path('', apis.UserList.as_view(), name='user-list'),
]
