from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import StaffProfileForm
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')  # Redirect to the home page after login
            else:
                # Authentication failed
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register_staff(request):
    if request.method == 'POST':
        
        form = StaffProfileForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to home.html if registration is successful
            return redirect('index')
    else:
        form = StaffProfileForm()
    
    # If form is not valid or it's a GET request, render signup.html with the form
    return render(request, 'signup.html', {'form': form})

# Create your views here.
def index(request):
   
    return render(request,"home.html")
def user_logout(request):
    logout(request)
    return redirect('login')