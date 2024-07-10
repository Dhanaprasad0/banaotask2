from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Patient, Doctor
from django.contrib.auth import get_user_model

User = get_user_model()

class PatientSignUpForm(UserCreationForm):
    medical_history = forms.CharField(widget=forms.Textarea, required=False)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'profile_picture', 'medical_history', 'address_line1','city','state','pincode')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        if commit:
            user.save()
            Patient.objects.create(user=user, medical_history=self.cleaned_data.get('medical_history'))
        return user

class DoctorSignUpForm(UserCreationForm):
    specialization = forms.CharField(max_length=100)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'profile_picture','specialization', 'address_line1','city','state','pincode')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        if commit:
            user.save()
            Doctor.objects.create(user=user, specialization=self.cleaned_data.get('specialization'))
        return user