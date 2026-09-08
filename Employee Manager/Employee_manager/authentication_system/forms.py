from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as djangovalidationerror

class RegisterUser(forms.ModelForm):

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Confirm password'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username','email','password','confirm_password']

        widgets = {
            'username':forms.TextInput(
                attrs={
                    'placeholder':'Enter username',
                }
            ),
            'email':forms.EmailInput(
                attrs={
                    'placeholder':'Enter email',
                }
            )
        }


    # validation

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already taken')

        return username


    def clean_password(self):
        pwd = self.cleaned_data.get('password')

        cleaned_data = super().clean()

        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        temp_user = User(username = username,email = email)


        try:
            validate_password(pwd,user=temp_user)
        except djangovalidationerror as error:
            raise forms.ValidationError(error)

        return pwd


class Login_form(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'enter username'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'enter password'
            }
        )
    )