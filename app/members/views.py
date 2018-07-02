import json

import requests
from django import forms
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.views import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from config import settings
from .forms import SignupForm


# Create your views here.
def login_view(request):
    print(request.POST)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:

            # --login 이 이뤄지는 과정 **중요
            # session_id값을 django_sessions테이블에 저장,
            # 데이터는 user와 연결됨
            # 이 함수 실행 후 돌려줄 HttpResponse에는 Set-Cookie헤더를 추가,
            # 내용은 sessionid=<session값>
            login(request, user)
            next = request.GET.get('next')
            if next:
                return redirect(next)
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


User = get_user_model()


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.signup()
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    return render(request, 'members/signup.html', context)


def profile(request, author):
    author = User.objects.get(username=author)
    # login_user = request.user
    # if login_user == author:
    #     return render(request, 'members/profile.html')
    # else:
    context = {
        'author': author,
    }
    return render(request, 'members/profile.html', context)


def withraw(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        print(User.objects.all())
        user.delete()
        print(User.objects.all())
        return redirect('posts:post-list')
    else:
        return HttpResponse('withraw')


def follow_toggle(request):
    # 수업 진행 중 끝
    pass

def facebook_login(request):
    # 템플릿에서 첫번째 과정을 거친 후 request에서 code 전달됨(authentication code)
    # 전달받은 인증 코드를 사용해서 access token 을 얻음
    code = request.GET.get('code')
    url = 'https://graph.facebook.com/v3.0/oauth/access_token'
    params = {
        'client_id': settings.FACEBOOK_APP_ID,
        'redirect_uri': 'http://localhost:8000/members/facebook-login/',
        'client_secret': settings.FACEBOOK_APP_SECRET_CODE,
        'code': code,
    }
    # access code를 받기위해 다시 요청을 보냄
    # 클라이언트 아이디, 리다이렉트 uri에 덧붙여
    # 시크릿 코드와 전달받은 인증 코드를  params에 덧붙여 보낸다
    response = requests.get(url, params)
    # 제이슨은 텍스트로 전달된 엑세스 토큰을 딕트 형태로 변환 시켜주는 파이선 모듈이다
    # 제이슨을 통해서 토큰을 변수에 할당
    response_dict = json.loads(response.text)
    response_dict = response.json()
    access_token = response_dict['access_token']

    # 얻은 토큰을 통해 해당 사용자 고유의 user_id를 받을 수 있다
    # 얻은 토큰을 디버그 해주는 과정
    url = 'https://graph.facebook.com/debug_token'
    params = {
        'input_token': access_token,
        'access_token': f'{settings.FACEBOOK_APP_ID}|{settings.FACEBOOK_APP_SECRET_CODE}',
    }
    # response에는 기본적인 유져 프로필과 같은 사항이 담기게 된다
    response = requests.get(url, params)


    # 그래픽api를 통해서 추가적으로 필요한 정보를 탐색해본 후 얻어온다
    # 여기서부터는 그래픽 api 사용법 문서를 참고해서 진행함
    # email과 같이 그래픽에서 얻어오지 못한 것은 주소창의 스코프를 이용한다??
    url = 'https://graph.facebook.com/v3.0/me'
    params = {
        'access_token': access_token,
        'fields': ','.join([
            'id',
            'name',
            'first_name',
            'last_name',
            'picture',
        ])
    }
    # 필드의 정보를 담은 응답을 얻는다
    response = requests.get(url, params)
    response_dict = response.json()

    facebook_user_id = response_dict['id']
    first_name = response_dict['first_name']
    last_name = response_dict['last_name']
    url_img_profile = response_dict['picture']['data']['url']

    # 받은 정보를 get_or_create를 이용해 새로 유져를 생성한다
    # 여기서 - if문을 사용하지 않고 작성
    #       - default값으로 지정해주는 방법:
    #             get 에는 username만 사용되고 defaults로
    #             지정된 값들은 create 할 때 사용된다
    user, user_created = User.objects.get_or_create(
        username=facebook_user_id,
        defaults={
            'first_name': first_name,
            'last_name': last_name,
        },
    )
    login(request, user)
    return redirect('index')
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -

# 유져 클래스 자체를 가져올 때 get_user_model()
# foreign키에 user모델을 저장할 때는 settings.AUTH_USER_MODEL
def signup_bak(request):
    context = {
        'errors': [],
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        context['username'] = username
        context['email'] = email

        if User.objects.filter(username=username).exists():
            context['errors'].append('유져 이미 존재')
        if password != password2:
            context['errors'].append('다른 패스워드입니다')

        # for info in [('username', username), ('password', password), ('password2', password2), ('email', email)]:
        #     if not info[1]:
        #         context['errors'].append(f'tuple list - {info[0]} 를 입력해주세요')

        required_fields = {'username': {'verbose_name': '아이디'},
                           'password': {'verbose_name': '비밀번호'},
                           'password2': {'verbose_name': '비밀번호2'},
                           'email': {'verbose_name': '이메일'}
                           }
        for field_name in required_fields.keys():
            if not locals()[field_name]:
                context['errors'].append(
                    f"{required_fields[field_name]['verbose_name']} 입력해주세요")

        # for key, value in locals():
        #     if not value:
        #         context['errors'].append(f'locals() for문 - {key} 입력해주세요')

        # if not username:
        #     context['errors'].append('유져네임을 입력해주세요')
        # if not email:
        #     context['errors'].append('이메일을 입력해주세요')
        # if not password:
        #     context['errors'].append('패스워드을 입력해주세요')
        # if not password2:
        #     context['errors'].append('check password을 입력해주세요')

        if not context['errors']:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
            )

            # user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('index')
    return render(request, 'members/signup_bak.html', context)
