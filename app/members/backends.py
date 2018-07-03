import requests
from django.contrib.auth import get_user_model

from config import settings

User = get_user_model()


class FacebookBackend:
    def authenticate(self, request, code):
        """
        facebook의 authorization code가 주어졌을 때
        적절히 처리해서
        facebook의 user_id에 해당하는 User가 있으면
        해당 User를 리턴d
        :param request:
        :param code:
        :return:
        """

        def get_access_token(code):
            url = 'https://graph.facebook.com/v3.0/oauth/access_token'
            params = {
                'client_id': settings.FACEBOOK_APP_ID,
                'redirect_uri': 'http://localhost:8000/members/facebook-login/',
                'client_secret': settings.FACEBOOK_APP_SECRET_CODE,
                'code': code,
            }
            response = requests.get(url, params)

            response_dict = response.json()
            access_token = response_dict['access_token']
            return access_token

        def debug_token(token):
            url = 'https://graph.facebook.com/debug_token'

            params = {
                'input_token': token,
                'access_token': f'{settings.FACEBOOK_APP_ID}|{settings.FACEBOOK_APP_SECRET_CODE}',
            }
            response = requests.get(url, params)
            return response.json()

        def get_user_info(token, fields=('id', 'name', 'first_name', 'last_name', 'picture')):
            url = 'https://graph.facebook.com/v3.0/me'
            params = {
                'fields': ','.join(fields),
                'access_token': token,
            }
            response = requests.get(url, params)
            return response.json()

        def create_user_from_facebook_user_info(user_info):
            facebook_user_id = user_info['id']
            first_name = user_info['first_name']
            last_name = user_info['last_name']
            url_img_profile = user_info['picture']['data']['url']

            return User.objects.get_or_create(
                username=facebook_user_id,
                defaults={
                    'first_name': first_name,
                    'last_name': last_name,
                },
            )

        # code = request.GET.get('code')
        access_token = get_access_token(code)
        user_info = get_user_info(access_token)
        user, user_created = create_user_from_facebook_user_info(user_info)

        return user

    def get_user(self, user_id):
        """
        user_id(primary_key)값이 주어졌을 때, 해당 User인스턴스를 반환
        해당 User가 존재하면 반환하고, 없으면 None

        :param user_id: user모델의 primary_key값
        :return: primary_key에 해당하는 user가 존재하면 user인스턴스,아니면 none
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
