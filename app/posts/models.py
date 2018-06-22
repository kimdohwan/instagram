from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    # User.objects.create(username='superuser')

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        # on_delete=models.CASCADE,
        on_delete=models.SET_DEFAULT,
        default=4,
    )
    photo = models.ImageField(null=True)
    content = models.TextField(default='defalt값이 문자열로 설정되어있')
    created_at = models.DateTimeField(auto_now_add=True)
    test1 = models.CharField(max_length=1, editable=False)
    test2 = models.CharField(max_length=1)