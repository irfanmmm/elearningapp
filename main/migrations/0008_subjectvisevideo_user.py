# Generated by Django 4.2.7 on 2023-11-06 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_course_user_remove_subject_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectvisevideo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]