from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):

    class Meta:
        model= User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']


class UserUploadedItemForm(forms.ModelForm):
    class Meta:
                                                                                                    
        model = UserUploadedItem
        widgets = {
          'description': forms.Textarea(attrs={'rows':4, 'placeholder': 'Description of the Item', 'cols':15}),
          'price': forms.NumberInput(attrs={'min': 0, 'step': 0.01}),
          
        }
        
        exclude = ('user',) # excluding the user field from the form else form will not be valid
        fields = "__all__"