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

        # 정보 입력 오류 에러에 사용되는 변수: confirm_pw, username_list
        confirm_pw = request.POST['confirm_pw']
        username_list = [u.username for u in User.objects.all()]
        # 잘못된 정보 입력 시 에러메시지 출력 하기 위한 컨텍스트
        if password != confirm_pw or\
                not username or\
                username in username_list or \
                not password:
            context = {
                'input_id': username,
                'input_pw': password,
                'input_cpw': confirm_pw,
                'username_list': username_list,
                'existed_username_message': 'Error: existed ID',
                'wrong_pw_message': 'Error: not matched password',
                'no_name_message': 'Error: plz input ID',
                'no_password_message': 'Error: plz input PW'
            }
            return render(request, 'members/signup.html', context)

        # 새로운 유져 생성 및 인증,로그인
        else:
            User.objects.create_user(
                username=username,
                password=password,
            )
        # 잘 생성 되었는지 확인 및 로그인을 위한 함수: authenticate(), is_authenticated
        new_user = authenticate(request, username=username, password=password)
        login(request, new_user)
        return redirect('posts:post-list')
    else:
        return render(request, 'members/signup.html')
