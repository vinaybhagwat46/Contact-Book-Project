from django import forms
from .models import Contact,Contact_Group,User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

        def __str__(self):
            return self.username

class contactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"
    

class contact_group_form(forms.ModelForm):
    class Meta:
        model=Contact_Group
        fields="__all__"
    
        