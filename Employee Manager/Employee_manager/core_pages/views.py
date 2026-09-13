from django.shortcuts import render
from employee_app1.forms import Project
from django.contrib.auth.decorators import login_required
from authentication_system.custome import role_required

# Create your views here.
@login_required
@role_required
def admin_home_view(request):
    # list of all projects
    
    all_project = Project.objects.all()
    total_project = Project.objects.count()
    print(total_project)

    context = {
        'Projects':all_project
    }

    return render(request,'admin_home.html',context)
    



# -----employee home view-------
@login_required
def employee_home_view(request):
    employee = request.user.employee
    context = {
        'employee': employee,
        'department': employee.department,
        'profile': employee.profile,
        'projects': employee.project_set.all(),
    }
    return render(request, 'employee_home.html',context)
