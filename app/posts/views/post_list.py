from django.shortcuts import render

from posts.form import PostCommentModelForm
from posts.models import Post, PostComment

__all__ = (
    'post_list',
)


def post_list(request):
    posts = Post.objects.all()
    comments = PostComment.objects.all()
    form = PostCommentModelForm()
    context = {
        'posts': posts,
        'comments': comments,
        'form': form,
    }
    return render(request, 'posts/post_list.html', context)
