from dataclasses import fields
from multiprocessing.sharedctypes import Value
from tkinter import Widget
from django import forms
from .models import user

class studentregistration(forms.ModelForm):
    class Meta:
        model=user
        fields = ['Student_name','Class','roll_no']
        widget = {
            'Student_name': forms.TextInput(),
            'Class' : forms.NumberInput(),
            'roll_no' : forms.NumberInput(),
        }