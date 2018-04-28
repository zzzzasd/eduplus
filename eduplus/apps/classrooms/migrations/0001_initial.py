# Generated by Django 2.0.4 on 2018-04-23 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('class_name', models.CharField(choices=[('1 orkid', '1 Orkid'), ('1 ixora', '1 Ixora'), ('2 orkid', '2 Orkid'), ('2 ixora', '2 Ixora'), ('3 orkid', '3 Orkid'), ('3 ixora', '3 Ixora')], max_length=20)),
            ],
        ),
    ]