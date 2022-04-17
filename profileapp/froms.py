from django import forms
from django.db import transaction
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.db.models import fields

from accounts.models import Customer, PgOwner, User

class EditCustomerProfileForm(UserChangeForm):
    profile_pic = forms.ImageField()
    address = forms.CharField(max_length=150, widget=forms.TextInput(attrs = {'class':'form-control'}))
    contact_no = forms.CharField(max_length=15, widget=forms.TextInput(attrs = {'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('profile_pic', 'address', 'contact_no')

class EditOwnerProfileForm(UserChangeForm):
    PgOwner_pic = forms.ImageField()
    location = forms.CharField(max_length=200, widget=forms.TextInput(attrs = {'class':'form-control'}))
    contact_no = forms.CharField(max_length=50, widget=forms.TextInput(attrs = {'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('PgOwner_pic', 'location', 'contact_no')

class ProfileNameForm(UserChangeForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs = {'class':'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs = {'class':'form-control'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs = {'class':'form-control'}))

    
    class Meta:
        model = User
        fields = ('first_name', 'last_name','email')


