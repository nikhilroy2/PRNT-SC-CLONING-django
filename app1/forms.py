from django import forms
from .models import *
 
 
class GalleryForm(forms.ModelForm):
 
    class Meta:
        model = GalleryList
        fields = ['name', 'image']