from django.http import HttpResponse

def role_required(func):
       def wrapper(request,*args,**kwargs):
                if request.user.employee.role !='admin':
                     return HttpResponse("Access Denied !!!")
                return func(request,*args,**kwargs)
       return wrapper 
        
