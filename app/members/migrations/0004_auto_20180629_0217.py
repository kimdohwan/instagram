# Generated by Django 2.0.6 on 2018-06-29 02:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.fields.related
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20180629_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='relation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='relation',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.fields.related.ForeignKey, related_name='relations_by_to_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
