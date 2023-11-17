from django.contrib import admin
from django.urls import path ,include
from django.conf.urls.static import static
from . import settings 
from main.views import send_otp,verify_otp,course,subject,is_finished,login_attempt


urlpatterns = [
    path('admin/', admin.site.urls),
    path('send_otp/', send_otp),
    path('verify_otp/', verify_otp),
    path('subject/<int:pk>/', subject),
    path('course/', course),
    path('finished/<int:pk>/', is_finished,name='is_finished'),
    path('login_attempt/', login_attempt),
    path('api/auth/', include('api.auth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
