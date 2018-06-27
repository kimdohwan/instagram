from django import forms
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponse

User = get_user_model()


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
            }
        ),
        required=False
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
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
    introduce = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        required=False
    )
    site = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        required=False
    )
    img_profile = forms.ImageField()
    CHOICES_GENDER = (
        ('m', '남성'),
        ('f', '여성'),
        ('x', '선택안함'),
    )
    gender = forms.ChoiceField(
        widget=forms.Select(),
        choices=CHOICES_GENDER,
    )

    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username=data).exists():
            raise ValidationError('유져ID 이미존재')
        return data

    def clean(self):
        super().clean()
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']

        if password != password2:
            self.add_error('password2', '비밀번호 불일치')
        return self.cleaned_data

    def signup(self):
        # cleaned_data는 유효성 검사를 성공 햇을 때 사용하는 데이터
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        introduce = self.cleaned_data['introduce']
        site = self.cleaned_data['site']
        img_profile = self.cleaned_data['img_profile']
        gender = self.cleaned_data['gender']

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            introduce=introduce,
            site=site,
            img_profile=img_profile,
            gender=gender,
        )
        return user

# 1. post_create구현
#     사진 1장과 설명을 받음 (설명은 없어도 되나, 사진은 반드시 필요)
#     로그인 한 유저만 이 view에 접근할 수 있도록 login_required데코레이터 사용
#
# 2. post_delete구현
#     해당하는 Post의 author일 경우에만 지울 수 있도록 설정
#
# 3. signup에 추가필드 구현 (SignupForm에 추가 구현)
#     img_profile, introduce, gender, site
#         gender만 필수선택, 나머지는 입력 안 해도 되도록 한다.
#         gender는 <select>를 띄울 수 있도록 해본다. (built-in widget사용)
#
# 4. withdraw(회원탈퇴) view 구현
