from django import forms
from django.forms import ModelForm
from django.core import validators
from fourth_app.models import User

class contact_form(forms.ModelForm):
    #enter validator code here
    full_name = forms.CharField(validators=[validators.MinLengthValidator(2,message="Not enough characters for name!")])
    class Meta:
        model= User
        fields = ['full_name','email']

#Create a form
form = contact_form()

#create a form to change an existing record
editform = User.objects.get(pk=1)
form = contact_form(instance=editform)




