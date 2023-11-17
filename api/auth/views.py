import requests
import json
from main.serializer import UserProfileSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth import get_user_model
from main.models import UserProfile



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):

    user_profile_instance = UserProfile.objects.get(user=request.user)

    
    request_data = {'name': request.data.get('name', user_profile_instance.name)}

    
    serializer = UserProfileSerializer(instance=user_profile_instance, data=request_data, partial=True)

    if serializer.is_valid():
        serializer.save(user=request.user)  

        responsedata = {
            "status_code": 200,
            "message": "Successfully Added"
        }
        return Response(responsedata)
    else:
        return Response(serializer.errors, status=400)
   


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):

    instance = UserProfile.objects.filter(user=request.user)

    serializer = UserProfileSerializer(instance,many=True)

    response_data = {
        'status':6000,
        'data':serializer.data,
    }

    return Response(response_data)


  

   
