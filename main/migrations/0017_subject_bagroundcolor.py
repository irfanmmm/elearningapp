# Generated by Django 4.2.7 on 2023-11-13 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_course_bagroundcolor_subjectvisevideo_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='bagroundcolor',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
