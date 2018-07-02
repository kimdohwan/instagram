from django.conf import settings
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models

from members.models import User


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    photo = models.ImageField(upload_to='post', blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='like_posts',
    )

    class Meta:
        ordering = ['-pk']


class PostComment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_comments',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='my_comments',
    )
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='commnets',
    )

    def __str__(self):
        return f'post: {self.post.pk} author: {self.author.username}'
