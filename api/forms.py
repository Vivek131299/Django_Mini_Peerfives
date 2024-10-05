# forms.py
from django import forms
from .models import PeerUser

class PeerUserForm(forms.ModelForm):
    class Meta:
        model = PeerUser
        fields = ['name']  # You can add other fields as needed
