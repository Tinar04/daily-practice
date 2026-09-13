from django import forms
from .models import Employee,Department,Project,Profile
import re
from django.core.exceptions import ValidationError
from django.utils import timezone

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


        labels = {
            'name' : 'Employee Name',
            'department':'Choose Your Department',
            'salary':'Employee Salary',
            'email':'Employee Email',
        }

        widgets = {
            'name':forms.TextInput(
                attrs={
                    'placeholder':'Enter Name',
                    
                }
            ),


            'salary':forms.NumberInput(
                attrs = {
                    'placeholder':'Enter salary'

                }
            ),
            'email':forms.EmailInput(
                attrs = {
                    'placeholder':'Enter email'
                }
            )
        }

        help_texts = {
            'salary':'enter salary in rupees',
            'email':"enter a valid domain name eg 'dcl.in' "
        }

        error_messages = {
            'email':{
                'unique':'A employee with same email already exists',
                'domain':'This domain in not valid in company'
            }
        }


    def clean_name(self):
        name = self.cleaned_data.get('name')

        
        pattern = r"^[A-Za-z]+ [A-Za-z]+$"

        if not re.match(pattern,name):
            print('error')
            raise forms.ValidationError("please Enter a valid name")

        return name


    def clean_salary(self):
        salary = self.cleaned_data.get('salary')

        if salary<=0:
            print('errorr')
            raise forms.ValidationError("Salary cant be negative")

        return salary


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['d_name']

        labels = {
            'd_name':'Department name'           
       }
        widgets= {
            'd_name':forms.TextInput(
                attrs={
                    'placeholder':'Enter name',
                }
            )
        }



    def clean_d_name(self):
            d_name = self.cleaned_data.get('d_name')
    
            
            pattern = r"^[A-Za-z]+ [A-Za-z]+$"
    
            if not re.match(pattern,d_name):
                print('error')
                raise forms.ValidationError("please Enter a valid name")
    
            return d_name


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

        labels = {
            'p_name':'Project Name',
            'start_date':'Starting date',
            'deadline':'Ending date',
            'status':'current status',
            'employee':'Assigned employees'

        }

        widgets = {
            'p_name':forms.TextInput(
                    attrs={
                        'placeholder':'Enter project name'
                    }
                ),
            'start_date':forms.DateInput(
                    attrs={
                         'placeholder':'Enter start date',
                         'type':'date',
                         }
                    ),
                    

            'deadline':forms.DateInput(
                     attrs={
                         'placeholder':'Enter deadline',
                          'type':'date',
                     }
            ),
                    
            
                    
        }
    def clean_p_name(self):
            p_name = self.cleaned_data.get('p_name')
    
            
            pattern = r"^[A-Za-z]+ [A-Za-z]+$"
    
            if not re.match(pattern,p_name):
                print('error')
                raise forms.ValidationError("please Enter a valid name")
    
            return p_name
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        deadline = cleaned_data.get('deadline')

        if start_date and deadline:
            if start_date >= deadline:
                raise ValidationError("Deadline must be after the start date.")

        
        return cleaned_data

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['contact', 'address',]  

        widgets ={
            'contact':forms.TelInput(
                attrs={
                    'placeholder':'Enter contact',
                    'max_length':10,
                }
            ),
            'address':forms.Textarea(
                attrs={
                    'placeholder':'Enter address',
                    'row':6,
                    'col':10,
                }
            )
        }

        labels = {
            'contact':"employee Contact",
            'address':'Address'
        }