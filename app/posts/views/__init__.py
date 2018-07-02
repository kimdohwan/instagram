from .post_create import *
from .post_comment import *
from .post_delete import *
from .post_detail import *
from .post_like import *
from .post_list import *
from .comment_create import *









# @login_required
# def post_comment_bak(request, pk):
#     if request.method == 'POST':
#         post = Post.objects.get(pk=pk)
#         author = request.user
#         content = request.POST['content']
#
#         PostComment.objects.create(
#             post=post,
#             author=author,
#             content=content,
#         )
#     return redirect('posts:post-list')




# -------------------------------------------------------------


# @login_required
# def post_create_with_form(request):
#     if request.method == 'POST':
#         form = CreateForm(request.POST, request.FILES)
#         if form.is_valid():
#             author = request.user
#             form.post_create(author)
#             return redirect('posts:post-list')
#     else:
#         form = CreateForm()
#
#     context = {
#         'form': form
#     }
#     return render(request, 'posts/post_create.html', context)


# def post_delete(request, pk):
#     print(request.user.is_authenticated)
#     if request.method == 'POST':
#         return HttpResponse
#     if request.user.is_authenticated:
#         return


# def my_post_delete(request, pk):
#     if request.method == 'POST':
#         post = Post.objects.get(pk=pk)
#         if post.author == request.user:
#             post.delete()
#             return redirect('posts:post-list')
#         else:
#             posts = Post.objects.all().order_by('-id')
#             context = {
#                 'posts': posts,
#                 'error': '너 삭제 못함',
#                 'post_id': post.id
#             }
#             return render(request, 'posts/post_list.html', context)
#     else:
#         return HttpResponse('get요청입니다')


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
