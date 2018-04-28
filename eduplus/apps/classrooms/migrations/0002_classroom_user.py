# Generated by Django 2.0.4 on 2018-04-23 15:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classrooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='user',
            field=models.ForeignKey(default='', on_delete='SET_NULL', to=settings.AUTH_USER_MODEL),
        ),
    ]
