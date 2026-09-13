from django.shortcuts import render
from employee_app1.forms import Project

# Create your views here.


def admin_home_view(request):
    # list of all projects
    
    all_project = Project.objects.all()
    total_project = Project.objects.count()
    print(total_project)

    context = {
        'Projects':all_project
    }

    return render(request,'admin_home.html',context)
    



