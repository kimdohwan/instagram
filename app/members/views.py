from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def login_view(request):
    print(request.POST)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('posts:post-list')
        else:
            return redirect('members:login')
    else:
        return render(request, 'members/login.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('posts:post-list')
    else:
        return redirect('members:login')


# sign up 으로 유져 생성 후 자동 로그인
# 그리고 index 로 redirect
def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_pw = request.POST['confirm_pw']
        if password != confirm_pw:
            context = {
                'wrong_pw_message': 'Error: password does not match',
                'input_id': username,
                'input_pw': password,
            }
            return render(request, 'members/signup.html', context)
            # return HttpResponse(context['wrong_pw'])
        else:
            User.objects.create_user(
                username=username,
                password=password,
            )
        new_user = authenticate(request, username=username, password=password)
        login(request, new_user)
        return redirect('posts:post-list')
    else:
        return render(request, 'members/signup.html')
