from django import forms
from .models import Task_Model


class Task_Form(forms.ModelForm):
    class Meta:
        model = Task_Model

        fields = '__all__'
        

        widgets = {
            'task_name':forms.TextInput(
                attrs={
                    "placeholder":"Enter Goal"
                }
            ),
            'task_description':forms.TextInput(
                attrs={
                    'placeholder':"Descripe your goal"
                }
            )
        }


        
