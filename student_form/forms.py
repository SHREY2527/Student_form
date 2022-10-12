from django import forms
from .models import Studentdetail
 
class studentform(forms.ModelForm):
    class Meta:
        model = Studentdetail
        fields = "__all__"