# Generated by Django 4.2.7 on 2023-11-05 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='learningl/thumbnailimage/')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectViseVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='learningl/videos/')),
                ('title', models.CharField(max_length=255)),
                ('is_finish', models.BooleanField(default=False)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='course/image/')),
                ('name', models.CharField(max_length=255)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subject')),
            ],
        ),
    ]