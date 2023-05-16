from django import forms

from app.models import *

class Userform(forms.ModelForm):
    class Meta():
        model=User
        fields=['username','password','email']
        widgets={'password':forms.PasswordInput()}

class Studentform(forms.ModelForm):
    class Meta():
        model=Student
        fields=['address','profile_pic']