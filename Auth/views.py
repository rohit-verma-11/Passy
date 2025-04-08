from django.shortcuts import render, redirect
from .models import Credentials
# Create your views here.

def signup(request):
    return render(request,'signup.html',{'error':None})


def login(request):
    return render(request,'login.html')

def verify(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        try:
            user = Credentials.objects.get(email=email, password=password)
            request.session['email'] = user.email    # Store user ID in session for later use
            print(user)
            request.session['password'] = user.password    # Store user name in session for later use
            return redirect('Dashboard')  # Redirect to the dashboard after successful login
        except Credentials.DoesNotExist:
            return redirect('Login')  # Redirect to login page if credentials are incorrect
    return redirect('login')  # Redirect to login page if the request method is not POST

def logout(request):
    try:
        del request.session['email']  # Remove user ID from session
        del request.session['password']  # Remove user name from session
    except KeyError:
        pass  # Ignore if the session variables do not exist
    return redirect('home')  # Redirect to home page after logout

def create(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('Password')
        print(email,password)
        try:
            user = Credentials.objects.create(email=email,password=password)
            user.save()
            return redirect('Login')  # Redirect to login page after successful signup
        except :
            return render(request,'signup.html',{'error':'Account already exists'})
    # Handle the case where the email already exists in the database
    return redirect('signup')  # Redirect to signup page if the request method is not POST