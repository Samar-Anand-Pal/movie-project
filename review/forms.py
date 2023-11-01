from django import forms
from .models import userinput

class UserInputForm(forms.ModelForm):
    class Meta:
        model = userinput
        fields = ['m_name', 'u_name', 'review', 'rating']
