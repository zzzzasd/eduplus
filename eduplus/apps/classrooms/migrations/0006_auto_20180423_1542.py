# Generated by Django 2.0.4 on 2018-04-23 15:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0005_auto_20180423_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='user',
            field=models.ForeignKey(default=None, on_delete='SET_NULL', to=settings.AUTH_USER_MODEL),
        ),
    ]
