# Generated by Django 2.0.4 on 2018-04-24 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_auto_20180424_0644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='classrooms',
        ),
    ]
