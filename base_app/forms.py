from dataclasses import field
from django import forms
from .models import Moment

class MomentForm(forms.ModelForm):
    class Meta:
        model = Moment
        fields = ('title', 'text', 'date')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control'}),
        }
    