# Generated by Django 2.0.4 on 2018-04-24 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_user_classrooms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='classrooms',
        ),
    ]
