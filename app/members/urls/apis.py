from django.urls import path

from ..apis import UserList

app_name = 'users_apis'
urlpatterns = [
    path('', UserList.as_view(), name='user-list'),
]
