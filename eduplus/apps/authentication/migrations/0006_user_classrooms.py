# Generated by Django 2.0.4 on 2018-04-24 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0011_classroom_users'),
        ('authentication', '0005_auto_20180423_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='classrooms',
            field=models.ManyToManyField(to='classrooms.Classroom'),
        ),
    ]
