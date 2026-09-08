from django.shortcuts import render,redirect
from .forms import RergisterUser,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def registration_view(request):
    form = RergisterUser()   #unbounded form

    if request.method =='POST':
        form = RergisterUser(data=request.POST)  #bounded form

        if form.is_valid():
            form.cleaned_data.pop('confirm_password')   #removing the confim password item 

            User.objects.create_user(**form.cleaned_data)  #hashing the password
            return redirect('login')


    context = {
        'form':form,
        'operation':'Register'
    }

    return render(request,'register_page.html',context)

# for resources login is required
@login_required
def home_view(request):
    return render(request,'home_page.html')

# login page

def login_view(request):


    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request,username = username,password = password)

            if user is not None:
                login(request,user)
                return redirect('home')

            form.add_error(None,'Invalid Credentials!!!')  #to create a non field error
    else:
        form = LoginForm()    #unbounded form for get method


    context = {
        'form':form,
        'operation':'Login'
    }
    return render(request,'Login_page.html',context)


# for logout login is required
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')