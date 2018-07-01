from django.urls import path
from . import views

app_name = 'members'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup_bak/', views.signup_bak, name='signup_bak'),
    path('signup/', views.signup, name='signup'),
    path('profile/<slug:author>', views.profile, name='profile'),
    path('withraw/<int:pk>', views.withraw, name='withraw'),

    path('talk/', views.talk, name='talk'),
    path('talk/detail/', views.talk_detail, name='talk-detail')
]