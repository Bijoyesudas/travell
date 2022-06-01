from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    if request.method == 'POST':
        uname = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass']
        cpassword = request.POST['cpass']
        if password == cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=uname, first_name=fname, last_name=lname, email=email,
                                                password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'check password ')
            return redirect('register')

    return render(request, 'register.html')


def login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        password=request.POST['pass']
        user=auth.authenticate(username=uname,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
             messages.info(request,"invalid credentials")
             return redirect('login')
    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

