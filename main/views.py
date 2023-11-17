from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from main.helpers import send_otp_to_phone
from main.models import Subject, User, Course, SubjectViseVideo, UserProfile
from main.serializer import (
    SubjectSerializer,
    CourseSerializer,
    SubjectViseVideoSerializer,
)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404


@api_view(["POST"])
@permission_classes([AllowAny])
def send_otp(request):
    data = request.data

    if data.get("phone_number") is None:
        return Response({"status": 400, "message": "Key phone no is requierd"})

    if data.get("password") is None:
        return Response({"status": 400, "message": "Key password no is requierd"})

    user = User.objects.create(
        phone_number=data.get("phone_number"),
        otp=send_otp_to_phone(data.get("phone_number")),
        username=data.get("phone_number"),
    )
    user.set_password = data.get("set_password")
    user.save()

    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    return Response(
        {"status": 200, "message": "Otp Sent", "access_token": access_token}
    )


@api_view(["POST"])
@permission_classes([AllowAny])
def verify_otp(request):
    print("Received data:", request.data)

    data = request.data

    otp = data.get("otp")

    print("Received OTP:", otp)

    if data.get("phone_number") is None:
        return Response({"status": 400, "message": "Key phone no is requierd"})

    if otp is None:
        return Response({"status": 400, "message": "Key OTP no is requierd"})

    try:
        user_obj = User.objects.get(phone_number=data.get("phone_number"))

    except Exception as e:
        return Response({"status": 400, "message": "Invalid Phon No"})

    if user_obj.otp == otp:
        user_obj.is_phone_verified = True
        user_obj.save()

        existing_profile = UserProfile.objects.filter(user=user_obj).first()

        if not existing_profile:
            new_profile = UserProfile.objects.create(user=user_obj)
            new_profile.save()

        refresh = RefreshToken.for_user(user_obj)
        access_token = str(refresh.access_token)

        response = Response(
            {
                "status": 200,
                "message": "Successfully verified",
                "access_token": access_token,
            }
        )

        response[
            "Access-Control-Expose-Headers"
        ] = "Authorization"  # Allow the front-end to access the Authorization header
        response["Authorization"] = f"Bearer {access_token}"
        return response

    else:
        return Response({"status": 400, "message": "Invalid OTP"})


# LOGIN
@api_view(["POST"])
@permission_classes([AllowAny])
def login_attempt(request):
    data = request.data

    phone_number = data.get("phone_number")

    if not phone_number:
        response_data = {
            "status_code": 6001,
            "message": "Phone Number Dosnot Enterd",
        }
        return Response(response_data)

    user = User.objects.filter(phone_number=phone_number).first()

    if user is None:
        response_data = {
            "status_code": 6001,
            "message": "User Desnot Exist",
        }
        return Response(response_data)

    else:
        user.otp = send_otp_to_phone(data.get("phone_number"))
        user.save()

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        response_data = {
            "status_code": 6000,
            "message": "User Desnot Exist",
            "data": access_token,
        }
        return Response(response_data)


# Normal Fields
# Course [ 4 ]
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def subject(request, pk):
    course = get_object_or_404(Course, pk=pk)

    subject = Subject.objects.filter(cource=course)

    context = {"request": request}
    serializer = SubjectSerializer(subject, many=True, context=context)

    response_data = {
        "status": 6000,
        "data": serializer.data,
    }
    return Response(response_data)


# Modules [ 10 ]
@api_view(["GET"])
@permission_classes([AllowAny])
def course(request):
    instance = Course.objects.all()

    context = {"request": request}

    serializer = CourseSerializer(instance, many=True, context=context)

    response_data = {
        "status": 6000,
        "data": serializer.data,
    }

    return Response(response_data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def is_finished(request, pk):
    try:
        subject_video_instance = get_object_or_404(SubjectViseVideo, pk=pk)

        # Assuming 'is_finish' is a ManyToManyField related to the user model
        if subject_video_instance.is_finish.filter(pk=request.user.pk).exists():
            subject_video_instance.is_finish.add(request.user)
            message = "is_finished"

            response_data = {"status_code": 6000, "message": message}
            return Response(response_data)
        else:
            subject_video_instance.is_finish.add(request.user)
            message = "is_finished"

            response_data = {"status_code": 6000, "message": message}
            return Response(response_data)

    except SubjectViseVideo.DoesNotExist:
        response_data = {"status_code": 6001, "message": "SubjectViseVideo not found."}
        return Response(response_data)
