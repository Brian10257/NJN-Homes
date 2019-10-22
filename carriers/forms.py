from django import forms
from django.forms import ClearableFileInput
from .models import Apply


class ApplyModelForm(forms.ModelForm):
    class Meta:
        model = Apply 
        fields = ['docs']
        widgets = {
            'docs': ClearableFileInput(attrs={'multiple': True})
        } 
        # widgets is important to upload multiple files 