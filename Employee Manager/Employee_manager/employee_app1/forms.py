from django import forms
from .models import Employee,Department
import re



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