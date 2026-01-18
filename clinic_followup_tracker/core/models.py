import secrets
from django.db import models
from django.contrib.auth.models import User


def generate_clinic_code():
    return secrets.token_hex(4)


def generate_public_token():
    return secrets.token_urlsafe(16)


class Clinic(models.Model):
    name = models.CharField(max_length=255)
    clinic_code = models.CharField(max_length=20, unique=True, default=generate_clinic_code, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class FollowUp(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('done', 'Done'),
    ]

    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    patient_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    language = models.CharField(max_length=2, choices=[('en', 'English'), ('hi', 'Hindi')])

    notes = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    public_token = models.CharField(max_length=50, unique=True, default=generate_public_token, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PublicViewLog(models.Model):
    followup = models.ForeignKey(FollowUp, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)
    user_agent = models.TextField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
