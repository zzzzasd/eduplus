# Generated by Django 2.0.4 on 2018-04-23 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0009_auto_20180423_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='user',
        ),
    ]