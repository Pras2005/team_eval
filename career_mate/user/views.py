from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from .models import User


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')

        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, email=email, phone_number=phone_number,  password=make_password(password))
                login(request, user)
                return redirect('login')  
            except Exception as e:
                error_message = str(e)
                return render(request, 'signup.html', {'error_message': error_message})
        else:
            error_message = "Passwords do not match"
            return render(request, 'signup.html', {'error_message': error_message})
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request ,'login.html')

def logout_view(request):
    logout(request)
    return redirect('landing')

def landing(request):
    return render(request, 'landing.html')

def home(request):
    return render(request, 'home.html')