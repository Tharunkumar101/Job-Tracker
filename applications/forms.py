from django import forms
from .models import JobApplication

class JobForm(forms.ModelForm):

    class Meta:
        model = JobApplication
        fields = ['company', 'role', 'applied_date', 'status', 'notes']
        widgets = {
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'applied_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }