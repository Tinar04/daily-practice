from django.shortcuts import render,redirect
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
                task_description = form.cleaned_data['task_description'],
                status = form.cleaned_data['status']
            )

        task = Task_Model.objects.all() 
        print(task,"hellooooooo") 
        form=Task_Form()
          
        context = {
            'tasks':task,
            'form':form,
            
        }
                
        return render(request,'Task_page.html',context)

   
    form=Task_Form()
    task = Task_Model.objects.all()
    print("inside get method...")


    context={
        'tasks':task,
        "form":form
    }

    return render(request,'Task_page.html',context)
    
            

        
# update operation


def update_task_view(request,task_id):
    try:
        task = Task_Model.objects.get(id = task_id)
    except Task_Model.DoesNotExist:
        return HttpResponse(
            ''' <h1 "style= color:red;">Student not found</h1>''')

    if request.method=='POST':
        form = Task_Form(data = request.POST,instance=task)

        if form.is_valid():
            task.task_name=form.cleaned_data['task_name']
            task.task_description = form.cleaned_data['task_description']
            task.status = form.cleaned_data['status']
            form.save()
            return redirect('task_form')

    # currentdata = {
    #     'task_name' : task.task_name,
    #     'task_description':task.task_description,
    #     'status':task.status
    # }
    form = Task_Form(instance=task)

    context = {
        'form':form
        
    }

    return render(request,'update_task.html',context)
        
        


def delete_task_view(request,task_id):
    try:
        task = Task_Model.objects.get(id = task_id)
    except Task_Model.DoesNotExist:
         return HttpResponse(
                    '''
                    <h1 "style= color:red;">Student not found</h1>
        
                    '''
                )
    if request.method == 'POST':
        task.delete()

        return redirect('task_form')
    
    context = {
        'task':task
    }
    return render(request,'delete_task.html',context)
    
