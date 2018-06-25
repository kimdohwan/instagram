from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponse


class SignupForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이메일',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호',
            }
        ),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username=data).exists():
            raise forms.ValidationError('유져ID 이미존재')
        return data

    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        print(cleaned_data)
        print(password)
        print(password2)

        if password != password2:
            print('패스워드 같지 않음')


            raise forms.ValidationError('비밀번호 불일치')
