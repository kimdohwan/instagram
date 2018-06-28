from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.decorators.http import require_POST

from .form import CreateForm, PostModelForm
from .models import Post

User = get_user_model()


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/post_list.html', context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'posts/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:post-list')
    else:
        form = PostModelForm()

    context = {
        'form': form
    }
    return render(request, 'posts/post_create.html', context)


@login_required
def post_create_with_form(request):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            author = request.user
            form.post_create(author)
            return redirect('posts:post-list')
    else:
        form = CreateForm()

    context = {
        'form': form
    }
    return render(request, 'posts/post_create.html', context)


# def post_delete(request, pk):
#     print(request.user.is_authenticated)
#     if request.method == 'POST':
#         return HttpResponse
#     if request.user.is_authenticated:
#         return



@login_required
@require_POST
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        raise PermissionDenied('지울 권한 없습니다')
    post.delete()
    return redirect('posts:post-list')


def my_post_delete(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        if post.author == request.user:
            post.delete()
            return redirect('posts:post-list')
        else:
            posts = Post.objects.all().order_by('-id')
            context = {
                'posts': posts,
                'error': '너 삭제 못함',
                'post_id': post.id
            }
            return render(request, 'posts/post_list.html', context)
    else:
        return HttpResponse('get요청입니다')


"""
1. post_create구현
    사진 1장과 설명을 받음 (설명은 없어도 되나, 사진은 반드시 필요)
    로그인 한 유저만 이 view에 접근할 수 있도록 login_required데코레이터 사용

2. post_delete구현
    해당하는 Post의 author일 경우에만 지울 수 있도록 설정

3. signup에 추가필드 구현 (SignupForm에 추가 구현)
    img_profile, introduce, gender, site
        gender만 필수선택, 나머지는 입력 안 해도 되도록 한다.
        gender는 <select>를 띄울 수 있도록 해본다. (built-in widget사용)

4. withdraw(회원탈퇴) view 구현
"""
