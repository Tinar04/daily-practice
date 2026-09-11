from .forms import EmployeeForm
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from authentication_system.custome import role_required
from .models import Employee
from django.http import HttpResponse
# -----Employee Table Crud For Admin---------



# -----------------display employees-----------------------------
@login_required
@role_required
def display_employee_view(request):
    # print("Entered the display view-----------------------------------------------------------------------------------------------")
    employee = Employee.objects.all()

    context = {
        'employees':employee,
    }
    return render(request,'display_employee.html',context)


# ------------ Add Employee------------------
@login_required
@role_required
def add_employee_view(request):
    if request.method == 'POST':
        form = EmployeeForm(data=request.POST)
        print(form)
        print("entering validation ")
        if form.is_valid():
            print("Validation completed")
            form.save()
            print("data saved succefully")
            return redirect('home')
        else:
            
            print("validation failing")

    else:
        form = EmployeeForm()   #unbounded form

    context = {
        'form':form,
        'operation':'Add Employee',
    }

    return render(request,'create_form.html',context)


# ------Update Employeeee-------
@login_required
@role_required
def update_employee_view(request,emp_id):
    try:
        employee = Employee.objects.get(id = emp_id)
    except Employee.DoesNotExist:
        return HttpResponse("Employe not found")

    
    if request.method=="POST":
        form=EmployeeForm(request.POST, instance= employee)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = EmployeeForm(instance=employee)
    context = {
        'form':form,
        'operation':'Update'
    }

    return render(request,'update_employee.html',context)


#-----delete---------

def delete_employee_view(request,emp_id):
    try:
        employee = Employee.objects.get(id = emp_id)
    except Employee.DoesNotExist:
        return HttpResponse("Employee Not Found")

    if request.method == "POST":
        employee.delete()
        return redirect('home')

    return render(request,'delete_employee.html')