from django.core.files.storage import FileSystemStorage
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


def post_create(request):
    if request.method == 'POST':
        username = request.user
        content = request.POST['content']
        photo = request.FILES['photo']
        print(f'{type(photo)}, {photo}')
        print(f'{content}')
        print(f'{username}, {type(request.user)}')

        photo = request.FILES['photo']
        fs = FileSystemStorage()
        print(fs)
        filename = fs.save(photo.name, photo)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        # return render(request, 'core/simple_upload.html', {
        #     'uploaded_file_url': uploaded_file_url
        # })
    # return render(request, 'core/simple_upload.html')

    #
        Post.objects.create(
            username=username,
            content=content,
            photo=photo,
        )
        return redirect('posts:post-list')
    else:
        # print(request.user)
        return render(request, 'posts/post_create.html')
    # return HttpResponse('create post page')
