from django import forms
from .models import StudentModel

class StudentFrom(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
