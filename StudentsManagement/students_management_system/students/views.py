from django.shortcuts import render,redirect
from .models import Students
from django.http import HttpResponse

# Create your views here.
def create_students_view(request):
    if request.method == "POST":
        name = request.POST.get('name',' ')
        age = request.POST.get('age',' ')
        roll= request.POST.get('roll',' ')
        marks = request.POST.get('marks',' ')
        subject = request.POST.get('subject',' ')

        Students.objects.create(
            name = name,
            age = age,
            roll = roll,
            marks = marks,
            subject = subject
        )
        return redirect("display")
    return render(request,'create_student.html')

def display_students_view(request):
    Student = Students.objects.all()

    context = {
        'students':Student
    }
    return render(request,'display_students.html',context)


def update_student_view(request,student_id):
    try:
        student = Students.objects.get(id = student_id)
        
    except Students.DoesNotExist:
        return HttpResponse(
            '''
            <h1 "style= color:red;">Student not found</h1>

            '''
        )

    if request.method == 'POST':
        student.name = request.POST.get('name',student.name)
        student.age = request.POST.get('age',student.age)
        student.roll = request.POST.get('roll',student.roll)
        student.marks = request.POST.get('marks',student.marks)
        student.subject = request.POST.get('subject',student.subject)

        student.save()

        return redirect('display')

    context = {
        'student':student
    }

    return render(request,'update_student.html',context)


