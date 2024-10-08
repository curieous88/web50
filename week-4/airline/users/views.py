from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    # If no user is signed in, return to login page:
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reversed("login"))
    return render(request, "users/user.html")

def login_view(request):
    return render(request, "users/login.html")

def logout_view(request):
    # Pass is a simple way to tell python to do nothing.
    