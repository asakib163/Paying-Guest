from django import forms
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Customer, PgOwner, User

class CustomerSignUpForm(UserCreationForm):
    first_name= forms.CharField(required=True)
    last_name = forms.CharField(required = True)
    profile_pic = forms.ImageField()
    address = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=50)
    contact_no = forms.CharField(max_length=15)
    
    class Meta(UserCreationForm.Meta):
        model = User
        
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email  = self.cleaned_data.get('email')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.profile_pic = self.cleaned_data.get('profile_pic')
        customer.address  = self.cleaned_data.get('address')
        customer.contact_no  = self.cleaned_data.get('contact_no')
        customer.save()
        return customer
        



class PgOwnerSignUpForm(UserCreationForm):
    first_name= forms.CharField(required=True)
    last_name = forms.CharField(required = True)
    PgOwner_pic = forms.ImageField()
    NID_pic = forms.ImageField()
    location = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=50)
    contact_no = forms.CharField(max_length=15)
    
    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_owner = True
        user.first_name  = self.cleaned_data.get('first_name')
        user.last_name  = self.cleaned_data.get('last_name')
        user.email  = self.cleaned_data.get('email')
        user.save()
        pOwner = PgOwner.objects.create(user=user)
        pOwner.PgOwner_pic  = self.cleaned_data.get('PgOwner_pic')
        pOwner.NID_pic  = self.cleaned_data.get('NID_pic')
        pOwner.location  = self.cleaned_data.get('location')
        pOwner.contact_no  = self.cleaned_data.get('contact_no')
        pOwner.save()
        return pOwner
