from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

__all__ = (
    'login_view',
)


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
