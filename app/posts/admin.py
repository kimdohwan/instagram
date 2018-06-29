from django.contrib import admin

# Register your models here.
from posts.models import Post, PostComment

admin.site.register(Post)
admin.site.register(PostComment)
