from django.urls import path
from .views import CustomUserAPIView
from . import views

urlpatterns = [
    path('profile/<int:pk>/', CustomUserAPIView.as_view(), name='user_profile'),
    path('verify-phone/', views.verify_phone_number, name='verify_phone_number'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('send-message/', views.send_message, name='send_message'),
    path('get-messages/', views.get_messages, name='get_messages'),
    path('schedule-message/', views.schedule_message, name='schedule_message'),
    path('send-auto-messages/', views.send_auto_messages, name='send_auto_messages'),
    path('schedule-recurring-message/', views.schedule_recurring_message, name='schedule_recurring_message'),
    path('update-settings/', views.update_settings, name='update_settings'),
]