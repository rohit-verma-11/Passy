from django.shortcuts import render,redirect
from Auth.models import Passwords as passes

# Create your views here.
def index(request):
    try:
        email = request.session['email']
        password = request.session['password']
        print(email,password)
        return redirect('Dashboard')  # Redirect to the dashboard after successful login
    except KeyError:
        return render(request,'index.html')

def dash(request):
    email = request.session['email']
    passess = passes.objects.filter(user=email)# will return all the passwords of the user
    #to be completed
    context = {}
    try:
        data = passes.objects.get(user=email)
        context['data'] = data
        print(data)
    except:
        print(context) 
    print(passess)
    print(email)
    return render(request,'dash.html',{'name':'Passy'})