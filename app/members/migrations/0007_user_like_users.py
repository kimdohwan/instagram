# Generated by Django 2.0.6 on 2018-07-01 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20180628_1219'),
        ('members', '0006_auto_20180629_0619'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_users', to='posts.Post'),
        ),
    ]
