from django import forms
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.views import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
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
        user.delete()
        print(User.objects.all())
        return redirect('posts:post-list')
    else:
        return HttpResponse('withraw')


def follow_toggle(request):
    pass


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
