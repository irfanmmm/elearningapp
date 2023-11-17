# Generated by Django 4.2.7 on 2023-11-06 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_chapter_course_subject_alter_course_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='subject',
        ),
        migrations.AddField(
            model_name='subject',
            name='cource',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.course'),
            preserve_default=False,
        ),
    ]
