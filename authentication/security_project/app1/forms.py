from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as djangovalidationError


class RergisterUser(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Confirm the password'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username','email','password','confirm_password']


        widgets = {
            'username':forms.TextInput(
                attrs={
                    'placeholder':'Enter the username',
                }
            ),

            'email':forms.EmailInput(
                attrs={
                    'placeholder':'Enter email'
                }
            ),

            'password':forms.TextInput(
                attrs={
                    'placeholder':'Enter the password'
                }
            ),
            'confirm_password':forms.TextInput(
                attrs={
                    'placeholder':'Enter password again'
                }
            )
        }
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username = username).exists():
            raise forms.ValidationError('usrname already taken')
        return username


    def clean_password(self):
        pwd = self.cleaned_data.get('password')

        cleaned_data = super().clean()

        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        temp_user = User(username=username,email = email)   #just for checking purpose 

        try:
            validate_password(pwd,user= temp_user)
        except djangovalidationError as error:
            raise forms.ValidationError(error)
        return pwd

    def clean(self):
        attrs = super().clean()

        pwd = attrs.get('password')
        con_pwd = attrs.get('confirm_password')

        if pwd!= con_pwd:
            self.add_error('confirm_password','password mismatch')



class LoginForm(forms.Form):
    username = forms.CharField(
        widget  = forms.TextInput(
            attrs={
                'placeholder':'Enter the  username'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Enter the passsword'
            }
        )
    )