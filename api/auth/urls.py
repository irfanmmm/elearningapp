from django.urls import path 
from api.auth import views


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('create/', views.create),
    path('get_user/', views.get_user)

]