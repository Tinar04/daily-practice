from django.shortcuts import render
from employee_app1.forms import Project
from django.contrib.auth.decorators import login_required
from authentication_system.custome import role_required
from django.core.paginator import Paginator
from employee_app1.models import Employee,Department

# Create your views here.
@login_required
@role_required
def admin_home_view(request):
    all_project = Project.objects.all()
    paginator = Paginator(all_project, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    total_employees = Employee.objects.count()
    total_departments = Department.objects.count()
    total_projects = Project.objects.count()

    context = {
        'Projects': page_obj,
        'total_employees': total_employees,
        'total_departments': total_departments,
        'total_projects': total_projects,
    }
    return render(request, 'admin_home.html', context)



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
