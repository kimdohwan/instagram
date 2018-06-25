from django.contrib.auth import login, authenticate, get_user_model
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


# 유져 클래스 자체를 가져올 때 get_user_model()
# foreign키에 user모델을 저장할 때는 settings.AUTH_USER_MODEL
User = get_user_model()


def signup(request):
    context = {
        'errors': [],
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        context['username']: username
        context['email']: email

        if User.objects.filter(username=username).exists():
            context['errors'].append('유져 이미 존재')
        if password != password2:
            context['errors'].append('다른 패스워드입니다')

        if not context['errors']:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
            )

            # user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('index')
    return render(request, 'members/signup.html', context)
