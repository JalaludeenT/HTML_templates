from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth

from django.shortcuts import HttpResponse


# Create your views here.

def login(request):
    if request.method == 'POST':
        USERNAME = request.POST['Username']
        PASSWORD = request.POST['Password']
        user = auth.authenticate(username=USERNAME, password=PASSWORD)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid username and password')
            return redirect('login')
    return render(request, "login.html")


def registration(request):
    if request.method == 'POST':
        USERNAME = request.POST['Username']
        FIRST_NAME = request.POST['First_Name']
        LAST_NAME = request.POST['Last_Name']
        EMAIL = request.POST['Email']
        PASSWORD = request.POST['Password']
        CONFORM_PASSWORD = request.POST['Conform_password']
        if PASSWORD == CONFORM_PASSWORD:
            if User.objects.filter(username=USERNAME).exists():
                messages.info(request, 'Error: That username is already taken')
                return redirect('register')
            elif User.objects.filter(email=EMAIL).exists():
                messages.info(request, 'E-mail id is already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=USERNAME, email=EMAIL, password=PASSWORD,
                                                first_name=FIRST_NAME, last_name=LAST_NAME)
                user.save()
                messages.success(request, 'Successfully Created an Account')
                print('user registered')
                return redirect('login')
        else:
            messages.error(request, 'Check Password')
            return redirect('register')
        return redirect('/')
    return render(request, 'registration.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
