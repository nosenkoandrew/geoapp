from django import forms
from .models import Markers


class MarkersForm(forms.ModelForm):
    class Meta:
        model = Markers
        fields = ['address', 'desc',]