from django.shortcuts import render
from .mock_data import COURSES

# Create your views here.
def display_course_view(request):
    context ={
        'courses':COURSES
    }
    return render(request,'display_courses.html',context)

def details_of_course_view(request,code_id):
    for code,course in COURSES.items():
        if code.lower() == code_id.lower() :
            data = course
            break
    else:
        data = None
    context = {
        'course':data
    }
    return render(request,'details_of_course.html', context)
