# Generated by Django 4.2.7 on 2023-11-06 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_user_name_user_passwo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='passwo',
        ),
    ]
