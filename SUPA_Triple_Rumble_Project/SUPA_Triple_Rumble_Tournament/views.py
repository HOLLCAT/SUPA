from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):

    return render(request, 'SUPA_Triple_Rumble_Tournament/homepage.html')


def about(request):
    return render(request, 'SUPA_Triple_Rumble_Tournament/about.html')


def staff(request):
    return HttpResponse("Staff.")


def profile(request):
    return HttpResponse("Profile.")


def staff_profile(request):
    return HttpResponse("Staff Profile.")


def login(request):
    return HttpResponse("Login.")


@login_required
def logout(request):
    return HttpResponse("Logout.")


def sign_up(request):
    return HttpResponse("Sign up.")


def teams(request):
    return render(request, 'SUPA_Triple_Rumble_Tournament/teams.html')


def create_team(request):
    return HttpResponse("Create a team.")


def tournaments(request):
    return render(request, 'SUPA_Triple_Rumble_Tournament/tournaments.html')
