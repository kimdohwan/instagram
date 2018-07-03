from django.contrib.auth import login, get_user_model
from django.http import HttpResponse
from django.shortcuts import redirect, render

User = get_user_model()
__all__ = (
    'profile',
    'withraw',
)


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
