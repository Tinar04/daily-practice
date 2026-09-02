from django import forms
from .models import EmployeeModel


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = '__all__'


        lables = {
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

        error_message = {
            'email':{
                'unique':'A employee with same email already exists',
                'domain':'This domain in not valid in company'
            }
        }
