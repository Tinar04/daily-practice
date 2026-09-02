from django.shortcuts import render,redirect
from .models import EmployeeModel
from .forms import EmployeeForm
from django.http import  HttpResponse

# display view
def display_employee_view(request):
    employee = EmployeeModel.objects.all()

    context = {
        'employees':employee
    }
    return render(request,'display_employe.html',context)


def create_employee_view(request):
    if request.method =="POST":               #to save data in the database
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('display')
    else:       #get method to fetch the empty form 
        form = EmployeeForm()

    context = {
        'form':form
    }

    return render(request,'create_form.html',context)

def update_employee_View(request,emp_id):
    try:
        employee = EmployeeModel.objects.get(id = emp_id)
    except:
        return HttpResponse('''

       <h1 "style = color:red; ">Employee Not Found </h1>
     ''')

    # post method bounded form
    if request.method == "POST":

        form  = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('display')
        



    # get method unbounded form with previous data
    currentdata = {
        'name':employee.name,
        'department':employee.department,
        'salary':employee.salary,
        'email':employee.email
    }
    form = EmployeeForm(data = currentdata)

    context = {
        'form':form
    }

    return render(request,'update_employee.html',context)