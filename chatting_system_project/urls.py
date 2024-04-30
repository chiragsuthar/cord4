from django.urls import path, include

urlpatterns = [
    path('api/', include('chatting_system.urls')),
]
