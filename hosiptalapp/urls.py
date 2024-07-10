
from django.urls import path,include
from . import views

app_name = 'hosiptalapp'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls'))
]