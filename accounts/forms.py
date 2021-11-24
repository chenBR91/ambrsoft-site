from django import forms
from . import models


class CreateUserDetail(forms.ModelForm):
    class Meta:
        model = models.UserDetails
        fields = ['phone', 'city', 'age']



class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    address = forms.CharField(
        label= 'Adress',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_line2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    
    class Meta:
        model = models.Customer
        fields = ['first_name', 'last_name', 'email', 'city', 'address', 'address_line2', 'telephone', 'zip_code', 'state']
        
