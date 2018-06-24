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
            context = {
                'wrong_input': "Error: Can't sign in"
            }
            return render(request, 'members/login.html', context)
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
        # if password != confirm_pw:
        #     context = {
        #         'wrong_pw_message': 'Error: not matched password',
        #         'input_id': username,
        #         'input_pw': password,
        #     }
        #     return render(request, 'members/signup.html', context)
        # elif not username:
        #     context = {
        #         'no_name_message': 'Error: plz input ID'
        #     }
        #     return render(request, 'members/signup.html', context)

        # if username in [i.username for i in User.objects.all()]:
        #     context = {
        #         'existed_name': 'Error: existed id',
        #         'username_list': [i.username for i in User.objects.all()],
        #     }
        #     return render(request, 'members/signup.html', context)
        if password != confirm_pw or\
                not username or\
                username in [u.username for u in User.objects.all()] or \
                not password:
            context = {
                'wrong_pw_message': 'Error: not matched password',
                'input_id': username,
                'input_pw': password,
                'input_cpw': confirm_pw,
                'no_name_message': 'Error: plz input ID',
                'existed_username': 'Error: existed ID',
                'username_list': [i.username for i in User.objects.all()],
                'no_password_message': 'Error: plz input PW'
            }
            return render(request, 'members/signup.html', context)
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
