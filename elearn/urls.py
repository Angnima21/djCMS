from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
   # Shared URLs
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('services/', views.services, name='services'),
path('contact/', views.contact, name='contact'),

path('lsign/', views.LearnerSignUpView.as_view(), name='lsign'),
]
