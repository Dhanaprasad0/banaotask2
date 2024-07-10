from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from .forms import PatientSignUpForm, DoctorSignUpForm
from .models import Patient, Doctor
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

User = get_user_model()
def signup(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'patient':
            form = PatientSignUpForm(request.POST, request.FILES)
        elif form_type == 'doctor':
            form = DoctorSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            '''if user.is_patient:
                return redirect('patient_dashboard')
            elif user.is_doctor:
                return redirect('doctor_dashboard')
                # Handle other user types or redirect to a generic dashboard'''
            return redirect('hosiptalapp:dashboard')
    else:
        patient_form = PatientSignUpForm()
        doctor_form = DoctorSignUpForm()
    return render(request, 'registration/signup.html', {'patient_form': patient_form, 'doctor_form': doctor_form})

@login_required
def dashboard(request):
    user=request.user
    '''if isinstance(user, AnonymousUser):
        return redirect('login')
'''
    if request.user.is_authenticated:
        if user.is_patient:
            patient = Patient.objects.get(user=user)
            return render(request, 'registration/patient_dashboard.html', {'user': user, 'patient': patient})
        elif user.is_doctor:
            doctor = Doctor.objects.get(user=user)
            return render(request, 'registration/doctor_dashboard.html', {'user': user, 'doctor': doctor})
        return redirect('hosiptalapp:login')


def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
                if user.is_patient:
                    return redirect('dashboard')
                elif user.is_doctor:
                    return redirect('dashboard')
                else:
                    pass
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('hosiptalapp:login')