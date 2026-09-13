from .forms import EmployeeForm,DepartmentForm,ProjectForm,ProfileForm
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from authentication_system.custome import role_required
from .models import Employee,Department,Project
from django.http import HttpResponse
# -----Employee Table Crud For Admin---------



# -----------------display employees-----------------------------
@login_required
@role_required
def display_employee_view(request):
    employee = Employee.objects.all()
    departments = Department.objects.all()

    search = request.GET.get('search')
    department_id = request.GET.get('department')

    if search:
        employee = employee.filter(name__icontains=search)

    if department_id:
        employee = employee.filter(department_id=department_id)

    context = {
        'employees': employee,
        'departments': departments
    }
    return render(request, 'display_employee.html', context)


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

    return render(request,'update.html',context)


#-----delete---------

def delete_employee_view(request,emp_id):
    try:
        employee = Employee.objects.get(id = emp_id)
    except Employee.DoesNotExist:
        return HttpResponse("Employee Not Found")

    if request.method == "POST":
        employee.username.delete()   #delete from auth_user as well
        employee.delete()
        return redirect('display_emp')
    context = {
        'object':employee.name
    }

    return render(request,'delete.html')

# -----Department Table Crud For Admin---------

# show all tables
@login_required
@role_required
def department_list(request):
    department = Department.objects.all()
    print(department)


    context = {
        'departments':department
    }

    return render(request,'department.html',context)

# add department
@login_required
@role_required
def create_department(request):

    if request.method =="POST":
        form= DepartmentForm(data=request.POST)

        if form.is_valid():
            form.save()
            print("data stroed succefully")
            return redirect('display_table')
        else:
            print("validation failed")
    else:
        form = DepartmentForm() #unbounded form
          
            

    context = {
        'form':form,
        'operation':'Add department'
    }

    return render(request,'create_form.html',context)





#update on deparment table---------------------------
@login_required
@role_required
def update_department(request,dept_id):
    try:
        department = Department.objects.get(id = dept_id)
    except Department.DoesNotExist:
        return HttpResponse("Department not found")
        
    if request.method=='POST':
        form = DepartmentForm(request.POST,instance= department)

        if form.is_valid():
            form.save()
            return redirect('display_table')
    else:
        form = DepartmentForm(instance=department)
    context = {
        'form':form,
        'operation':'Update department',
    }

    return render(request,'update.html',context)

# -----delete-----
@login_required
@role_required
def delete_department(request,dept_id):

    try:
        department = Department.objects.get(id = dept_id)
    except Department.DoesNotExist:
        return HttpResponse("Department not found")

    if request.method == "POST":

        department.delete()
        return redirect('display_table')
    context = {
        'object':department.d_name
    }
    return render(request,'delete.html',context)

    
# -----projects lists------
#------display-------



# ------create a project-------
@login_required
@role_required
def create_project(request):
    if request.method=='POST':
        form = ProjectForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("data saved succefully")
        else:
            print("Validation")
    else:
        form = ProjectForm()   #unbounded form


    context = {
        'form':form,
        'operation':'Add Project',

    }

    return render(request,'create_form.html',context)

# -----display a single project-------
@login_required
@role_required
def display_one_project(request,p_id):
    try:
        project = Project.objects.get(id=p_id)
    except Project.DoesNotExist:
        return HttpResponse("Project Not found")

    context = {
        'project':project
    }
    return render(request,'view_one_project.html',context)


# --------udate a project------
@login_required
@role_required
def update_project_view(request,p_id):
    try:
        project = Project.objects.get(id = p_id)
    except Project.DoesNotExist:
        return HttpResponse("project not found")
        
    if request.method=='POST':
        form = ProjectForm(request.POST,instance=project)

        if form.is_valid():
            form.save()
            return redirect('admin-home')
    else:
        form = form = ProjectForm(instance=project)
    context = {
        'form':form,
        'operation':'Update project',
    }

    return render(request,'update.html',context)

#  ------delete a project----------------
@login_required
@role_required
def delete_project_view(request,p_id):
    try:
        project = Project.objects.get(id = p_id)
    except Project.DoesNotExist:
        return HttpResponse("Project Not Found")

    if request.method == "POST":
        
        project.delete()
        return redirect('admin-home')
    context = {
        'object':project.p_name
    }

    return render(request,'delete.html',context)



# -------employee viewssssss-----------------------

@login_required
def employee_profile_view(request):
    employee = request.user.employee
    profile = employee.profile
    context = {'employee': employee, 'profile': profile}
    return render(request, 'employee_profile.html', context)

@login_required
def update_profile(request):
    profile = request.user.employee.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    context = {'form': form,
               'operation':'Apply changes'}
    return render(request, 'update.html', context)