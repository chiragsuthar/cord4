from django.shortcuts import render
from rest_framework import generics
from .models import RecurringMessage, ScheduledMessage, UserProfile, UserSettings
from .serializers import UserProfileSerializer
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django_otp import devices_for_user
from django_otp.plugins.otp_static.models import StaticDevice
from .models import Message
from django.contrib.auth import get_user_model

class UserProfileAPIView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

@login_required
def verify_phone_number(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        if phone_number:
            user = request.user
            user.phone_number = phone_number
            user.save()

            # Create or update static device (phone number-based) for OTP verification
            device, created = StaticDevice.objects.get_or_create(user=user, name='phone_number', defaults={'number': phone_number})
            if not created:
                device.number = phone_number
                device.save()

            # Send OTP via SMS (simulated here)
            otp = '123456'  # Generate OTP dynamically
            # In a real scenario, you might send the OTP via SMS using a service like Twilio or AWS SNS
            # Here, we'll just return the OTP for demonstration
            return JsonResponse({'status': 'OTP sent to your phone number.', 'otp': otp})
        else:
            return JsonResponse({'error': 'Phone number is required.'}, status=400)
    return render(request, 'verify_phone_number.html')

@login_required
def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        if otp:
            user = request.user
            devices = devices_for_user(user)
            for device in devices:
                if device.verify_token(otp):
                    return JsonResponse({'status': 'OTP verified successfully.'})
            return JsonResponse({'error': 'Invalid OTP.'}, status=400)
        else:
            return JsonResponse({'error': 'OTP is required.'}, status=400)
    return render(request, 'verify_otp.html')

@login_required
def update_profile(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        profile_picture = request.FILES.get('profile_picture')

        if name:
            user.name = name
        if profile_picture:
            user.profile_picture = profile_picture

        user.save()

        return JsonResponse({'status': 'Profile updated successfully.'})
    return JsonResponse({'error': 'POST method required.'}, status=400)

@login_required
def send_message(request):
    if request.method == 'POST':
        sender = request.user
        receiver_id = request.POST.get('receiver_id')
        content = request.POST.get('content')

        if receiver_id and content:
            receiver = get_user_model().objects.get(id=receiver_id)
            message = Message.objects.create(sender=sender, receiver=receiver, content=content)
            return JsonResponse({'status': 'Message sent successfully.'})
        else:
            return JsonResponse({'error': 'Receiver ID and message content are required.'}, status=400)
    return JsonResponse({'error': 'POST method required.'}, status=400)

@login_required
def get_messages(request):
    if request.method == 'GET':
        user = request.user
        messages_sent = Message.objects.filter(sender=user)
        messages_received = Message.objects.filter(receiver=user)
        return JsonResponse({
            'sent_messages': list(messages_sent.values()),
            'received_messages': list(messages_received.values())
        })
    return JsonResponse({'error': 'GET method required.'}, status=400)

@login_required
def schedule_message(request):
    if request.method == 'POST':
        sender = request.user
        receiver_id = request.POST.get('receiver_id')
        content = request.POST.get('content')
        scheduled_time = request.POST.get('scheduled_time')

        if receiver_id and content and scheduled_time:
            receiver = get_user_model().objects.get(id=receiver_id)
            scheduled_message = ScheduledMessage.objects.create(sender=sender, receiver=receiver, content=content, scheduled_time=scheduled_time)
            return JsonResponse({'status': 'Message scheduled successfully.'})
        else:
            return JsonResponse({'error': 'Receiver ID, message content, and scheduled time are required.'}, status=400)
    return JsonResponse({'error': 'POST method required.'}, status=400)

@login_required
def send_auto_messages(request):
    # Implement logic to send auto messages for events
    # For example, you can retrieve upcoming events and send messages accordingly
    return JsonResponse({'status': 'Auto messages sent successfully.'})

@login_required
def schedule_recurring_message(request):
    if request.method == 'POST':
        sender = request.user
        receiver_id = request.POST.get('receiver_id')
        content = request.POST.get('content')
        interval = request.POST.get('interval')

        if receiver_id and content and interval:
            receiver = get_user_model().objects.get(id=receiver_id)
            recurring_message = RecurringMessage.objects.create(sender=sender, receiver=receiver, content=content, interval=interval)
            return JsonResponse({'status': 'Recurring message scheduled successfully.'})
        else:
            return JsonResponse({'error': 'Receiver ID, message content, and interval are required.'}, status=400)
    return JsonResponse({'error': 'POST method required.'}, status=400)

@login_required
def update_settings(request):
    if request.method == 'POST':
        user = request.user
        auto_send_messages = request.POST.get('auto_send_messages')
        auto_send_recurring_messages = request.POST.get('auto_send_recurring_messages')

        settings, created = UserSettings.objects.get_or_create(user=user)
        if auto_send_messages:
            settings.auto_send_messages = auto_send_messages
        if auto_send_recurring_messages:
            settings.auto_send_recurring_messages = auto_send_recurring_messages
        settings.save()

        return JsonResponse({'status': 'Settings updated successfully.'})
    return JsonResponse({'error': 'POST method required.'}, status=400)