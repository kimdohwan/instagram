from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from .models import Post


def post_list(request):
    posts = Post.objects.all().order_by('-pk')
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

