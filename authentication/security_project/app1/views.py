from django.shortcuts import render,redirect
from .forms import RergisterUser
from django.contrib.auth.models import User

# Create your views here.


def registration_view(request):
    form = RergisterUser()   #unbounded form

    if request.method =='POST':
        form = RergisterUser(data=request.POST)  #bounded form

        if form.is_valid():
            form.cleaned_data.pop('confirm_password')   #removing the confim password item 

            User.objects.create_user(**form.cleaned_data)  #hashing the password
            return redirect('home')


    context = {
        'form':form,
        'operation':'Register'
    }

    return render(request,'register_page.html',context)

def home_view(request):
    return render(request,'home_page.html')