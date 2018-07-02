from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from posts.form import PostModelForm

__all__ = (
    'post_create',
)

@login_required
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