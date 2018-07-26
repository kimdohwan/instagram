from django.shortcuts import redirect


def index(request):
    return redirect('posts:post-list')


def link_api(request, api_type):
    API_TYPE = ['posts', 'users']
    if api_type in API_TYPE:
        return redirect('apis:post-list')
