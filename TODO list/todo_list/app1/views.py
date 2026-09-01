from django.shortcuts import render
from django.http import HttpResponse
from .forms import Task_Form
from .models import Task_Model

# Create your views here.
def task_form_view(request):
    if request.method=="POST":
        print("Post method started...")
        form = Task_Form(data=request.POST) #bounded form

        print("data inside form object")
        if form.is_valid():
            print("validation done",form.cleaned_data)
            Task_Model.objects.create(
                task_name = form.cleaned_data['task_name'],
                task_description = form.cleaned_data['task_description'])
            
            
            
            
        else:
            print('jaa validation sikh ke aa')

        context = {
            
        }
                
        return render(request,'task_card.html',context)

    else:
        form=Task_Form()
        print("inside get method...")


    context={
        "form":form
    }

    return render(request,'Task_page.html',context)
    
            

        

       

    # form = Task_Form()
    # context = {
    #     "form":form
    # }
    # return render(request,'Task_page.html',context)