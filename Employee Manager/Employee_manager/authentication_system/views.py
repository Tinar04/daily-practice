from django.shortcuts import render,redirect
from .forms import RegisterUser,Login_form
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

#login view

def login_view(request):
    form = Login_form()

    if request.method =='POST':
        form = Login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user =authenticate(request,username = username,password = password)
            print(user)
            return HttpResponse(f'Welcome Home !!! {user}')

    context = {
        'form':form,
        'operation':"Login"
    }

    return render(request,'login.html',context)


def registration_view(request):
    form = RegisterUser()

    if request.method =='POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.cleaned_data.pop('confirm_password')
            User.objects.create_user(**form.cleaned_data)
        return redirect('login')

    context = {
        'form':form,
        'operation':'Register',
    }
    return render(request,'register.html',context)


