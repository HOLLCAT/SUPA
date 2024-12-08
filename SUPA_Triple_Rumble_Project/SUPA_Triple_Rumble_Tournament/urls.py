from django.contrib import admin
from django.urls import path
from django.urls import include
from SUPA_Triple_Rumble_Tournament import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('staff/', views.staff, name='staff'),
    path('profile/', views.profile, name='profile'),
    path('profile/staff-ccount/', views.staff_profile, name='staff_profile'),
    path('login/', views.login, name='login'),
    path('login/staff-login', views.login, name='staff_login'),
    path('sign-up/', views.sign_up, name='register'),
    # teams urls
    path('teams/', views.teams, name='teams'),
    path('teams/create-a-team/', views.create_team, name='create_a_team'),

    # tournament urls
    path('tournaments/', views.tournaments, name='tournaments'),

]
