from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        uname = request.POST['user_name']
        pwd = request.POST['Pass']
        cpwd = request.POST['con_pass']
        if pwd == cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "Username already Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=uname, password=pwd)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not match')
            return redirect('register')
    return render(request, 'Registration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['pass']
        Login = auth.authenticate(username=username, password=password)
        if Login is not None:
            auth.login(request, Login)
            return redirect('/')
        else:
            messages.info(request, 'Invalid User')
            return redirect('login')

    return render(request, 'Login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')