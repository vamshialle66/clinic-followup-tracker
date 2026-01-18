from django import forms
from .models import FollowUp


class FollowUpForm(forms.ModelForm):
    class Meta:
        model = FollowUp
        fields = ['patient_name', 'phone', 'language', 'notes', 'due_date']

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit() or len(phone) < 10:
            raise forms.ValidationError("Enter a valid phone number")
        return phone
