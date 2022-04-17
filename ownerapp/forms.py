from django import forms
from django.forms.widgets import CheckboxInput
from .models import Post

class PostFrom(forms.ModelForm):
    class Meta:
        model = Post
        # fields = "__all__"
        fields = ( 'home_name','home_description','home_image','room_images1','room_images2','room_images3','PG_type','address', 'price_per_month', 'city','divisions','furniture','AC','fan','bed','light','wifi','parking','breakfast','lunch','dinner')
        # widgets = {
        #     furniture forms.ChoiceField(choices=[GEEKS_CHOICES], required=False),
        #     'AC':forms.CheckboxInput(attrs = {'class':'form-control'}),
        #     'fan':forms.CheckboxInput(attrs = {'class':'form-control'}),
        #     'bed':forms.CheckboxInput(attrs = {'class':'form-control'}),
        #     'light':forms.CheckboxInput(attrs = {'class':'form-control'}),
        #     'wifi':forms.CheckboxInput(attrs = {'class':'form-control'}),
        #     'parking':forms.CheckboxInput(attrs = {'class':'form-control'}),
        #     'breakfast':forms.CheckboxInput(attrs = {'class':'form-control'}),
        #     'lunch':forms.CheckboxInput(attrs = {'class':'form-control'}),
        #     'dinner':forms.CheckboxInput(attrs = {'class':'form-control'}),
        # }