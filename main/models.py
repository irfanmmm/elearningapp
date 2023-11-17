from django.db import models
from django.contrib.auth.models import AbstractUser
from main.manager import UserManager
from students import settings


class User(AbstractUser):
    phone_number = models.CharField(max_length=12, unique=True )
    is_phone_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    password=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
   

    def __str__(self):
        return self.name


class Subject(models.Model):
    
    subject = models.CharField(max_length=255)
    bagroundcolor = models.CharField(max_length=50)
    image = models.ImageField(upload_to='learningl/thumbnailimage/')
    cource = models.ForeignKey('main.Course', on_delete=models.CASCADE)
    def __str__(self):
        return self.subject



class SubjectViseVideo(models.Model):
    subject = models.ForeignKey('main.Subject', on_delete=models.CASCADE)
    
    video = models.FileField(upload_to='learningl/videos/')
    title = models.CharField(max_length=255)
    timestamp = models.CharField(max_length=50)
    is_finish = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='finished_videos')
    # is_finish = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Course(models.Model):
    image=models.ImageField(upload_to='course/image/')
    bagroundcolor = models.CharField(max_length=50)
    name=models.CharField(max_length=255)
    video_count=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


 