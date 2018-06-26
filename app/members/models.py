from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    CHOICES_GENDER = (
        ('m', '남성'),
        ('f', '여성'),
        ('x', '선택안함'),
    )
    img_profile = models.ImageField(upload_to='user', blank=True)
    site = models.URLField(blank=True)
    introduce = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=1, choices=CHOICES_GENDER)

    def __str__(self):
        return self.username

