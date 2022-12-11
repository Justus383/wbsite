from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import ProfileData
from .excelvalue import getvalue

# Create your views here.
def register(request):
   
    if request.method == 'POST':
        usernamereg = request.POST['username']
        emailreg = request.POST['email']
        passwordreg = request.POST['password']
        
        user = User.objects.create_user(usernamereg, emailreg, passwordreg)
        userlen = (len(User.objects.all()))
        print(userlen)
        ProfileData.objects.create(
               user=user, excelid=userlen)
        auth_login(request, user)

        
           
        print("logedin")
        return redirect('/logedin/')
            
        
    
    return render(request, 'home.html')

@login_required(login_url="/")
def logedin(request):

    if request.method == 'POST':
        logout(request)
        return redirect('/')
    exid = request.user.profiledata.excelid
    
    excelvalue1, excelvalue2 = getvalue(exid)
    context = {'excelvalue1': excelvalue1,
               'excelvalue2': excelvalue2}
    return render(request, 'logedin.html', context)

def login(request):
    if request.method == 'POST':
        usernamereg = request.POST['username']
        
        passwordreg = request.POST['password']
        user = authenticate(username=usernamereg,password=passwordreg)
        if user is not None:
            print("logedin")
            auth_login(request, user)
            return redirect('/logedin/')
        else: print("failed")
    return render(request, 'login.html')