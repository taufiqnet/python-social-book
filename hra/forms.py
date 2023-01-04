from django import forms
from .models import Department

class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department 
        fields = ['dept_no', 'dept_name']
        widgets = {
            'dept_no':forms.TextInput(attrs={'class':'form-control', 'id':'deptnoid'}),
            'dept_name':forms.TextInput(attrs={'class':'form-control', 'id':'deptnameid'}),
        }