from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from main.models import Subject, SubjectViseVideo, Course,UserProfile

class SubjectViseVideoSerializer(ModelSerializer):
    subject = serializers.SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = SubjectViseVideo
    
    def get_subject(self, instance):
        return instance.subject.subject
    

class SubjectSerializer(ModelSerializer):
    cource = serializers.SerializerMethodField()
    subjectvisevideo = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'cource', 'image', 'subject', 'subjectvisevideo', 'bagroundcolor')
        model = Subject

    def get_subjectvisevideo(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        videos = SubjectViseVideo.objects.filter(subject=instance)

        serializer = SubjectViseVideoSerializer(videos, many=True, context=context)
        video_data = serializer.data

        
        user_finished_videos = request.user.finished_videos.values_list('id', flat=True)

        for video in video_data:
            video['is_finished'] = video['id'] in user_finished_videos
        return video_data
    
    
    def get_cource(self, instance):
        return instance.cource.name
    
    
    

# Courses [ 4 ]
class CourseSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Course


class UserProfileSerializer(ModelSerializer):

    user = serializers.SerializerMethodField()


    class Meta:
        fields = '__all__'
        model = UserProfile


    def get_user(self,instance):
        return instance.user.phone_number

