from django.contrib import admin

# Register your models here.
from .models import CustomUser, Patient, Doctor

admin.site.register(CustomUser)
admin.site.register(Patient)
admin.site.register(Doctor)