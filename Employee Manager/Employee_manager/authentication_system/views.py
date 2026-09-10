from django.shortcuts import render,redirect
from .forms import RegisterUser,Login_form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

#login view

def login_view(request):
    if request.method == "POST":
        form = Login_form(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request,username = username,password = password)

            if user is not None:
                login(request,user)
                return redirect('home')

    else:
        form = Login_form()   #unbounded form

    context = {
        'form':form,
        'operation':'Login'
    }
    return render(request,'login.html',context)

@login_required
def registration_view(request):
    if request.method == 'POST':
        form = RegisterUser(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False) #give model object  # creates an object and return the object but not save it in table

            pwd = form.cleaned_data['password']
            user.set_password(pwd)
            user.save()


            login(request,user=user)
            
            return redirect('login')
        # else:
        #     print("validation failed")

    else:
        form = RegisterUser()   #unbounded

    context = {
        'form':form,
        'operation':'Register'
    }

    return render(request,'register.html',context)










def logout_view(request):
    logout(request)
    return redirect('login')




