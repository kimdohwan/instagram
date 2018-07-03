import requests
from django.contrib.auth import login, get_user_model, authenticate
from django.shortcuts import redirect

from config import settings

User = get_user_model()

__all__ = (
    'facebook_login',
)


def facebook_login(request):
    # def get_access_token(code):
    #     url = 'https://graph.facebook.com/v3.0/oauth/access_token'
    #     params = {
    #         'client_id': settings.FACEBOOK_APP_ID,
    #         'redirect_uri': 'http://localhost:8000/members/facebook-login/',
    #         'client_secret': settings.FACEBOOK_APP_SECRET_CODE,
    #         'code': code,
    #     }
    #     response = requests.get(url, params)
    #
    #     response_dict = response.json()
    #     access_token = response_dict['access_token']
    #     return access_token
    #
    # def debug_token(token):
    #     url = 'https://graph.facebook.com/debug_token'
    #
    #     params = {
    #         'input_token': token,
    #         'access_token': f'{settings.FACEBOOK_APP_ID}|{settings.FACEBOOK_APP_SECRET_CODE}',
    #     }
    #     response = requests.get(url, params)
    #     return response.json()
    #
    # def get_user_info(token, fields=('id', 'name', 'first_name', 'last_name', 'picture')):
    #     url = 'https://graph.facebook.com/v3.0/me'
    #     params = {
    #         'fields': ','.join(fields),
    #         'access_token': token,
    #     }
    #     response = requests.get(url, params)
    #     return response.json()
    #
    # def create_user_from_facebook_user_info(user_info):
    #     facebook_user_id = user_info['id']
    #     first_name = user_info['first_name']
    #     last_name = user_info['last_name']
    #     url_img_profile = user_info['picture']['data']['url']
    #
    #     return User.objects.get_or_create(
    #         username=facebook_user_id,
    #         defaults={
    #             'first_name': first_name,
    #             'last_name': last_name,
    #         },
    #     )
    #
    code = request.GET.get('code')
    user = authenticate(request, code=code)

    if user is not None:
        login(request, user)
        return redirect('index')
    return redirect('members:login')


