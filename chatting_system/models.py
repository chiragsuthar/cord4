from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

class Message(models.Model):
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"From {self.sender} to {self.receiver}: {self.content}"
    
class ScheduledMessage(models.Model):
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    receiver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='scheduled_messages')
    content = models.TextField()
    scheduled_time = models.DateTimeField()

    def __str__(self):
        return f"From {self.sender} to {self.receiver} at {self.scheduled_time}: {self.content}"
    
class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.name
    
class RecurringMessage(models.Model):
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    receiver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='recurring_messages')
    content = models.TextField()
    interval = models.CharField(max_length=50)  # e.g., 'daily', 'weekly', 'monthly'

    def __str__(self):
        return f"From {self.sender} to {self.receiver}: {self.content} (Interval: {self.interval})"
    
class UserSettings(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    auto_send_messages = models.BooleanField(default=True)
    auto_send_recurring_messages = models.BooleanField(default=True)

    def __str__(self):
        return f"Settings for {self.user}"
    