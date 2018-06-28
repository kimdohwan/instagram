from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.http import request

from .models import Post

User = get_user_model()


class PostModelForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            # 'author',
            'content',
            'photo',
        ]


class CreateForm(forms.Form):
    content = forms.CharField(required=False)
    photo = forms.ImageField(required=False)

    # created_at = forms.DateTimeField()

    def post_create(self, author):
        author = author
        content = self.cleaned_data['content']
        photo = self.cleaned_data['photo']

        data = Post.objects.create(
            author_id=author.pk,
            content=content,
            photo=photo,
        )
        return data

    def clean_photo(self):
        data = self.cleaned_data['photo']
        if not data:
            raise ValidationError('파일이 존재하지않습니다')
        return data

    def clean(self):
        super().clean()
