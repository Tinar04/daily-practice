from django.shortcuts import render
from .mock_data import COURSES

# Create your views here.
def display_course_view(request):
    context ={
        'courses':COURSES
    }
    return render(request,'display_courses.html',context)