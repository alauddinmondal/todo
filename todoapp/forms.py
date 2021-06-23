from django import forms
from django.forms import fields, models
from .models import Employee


class EmpregisterForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = '__all__'
        fields = ('fullname', 'emp_code', 'mobile', 'position')
        labels = {'fullname':'Your Full Name','emp_code':'Your Employee Code'}
    
    def __init__(self, *args, **kwargs):
        super(EmpregisterForm,self).__init__(*args, **kwargs)
        self.fields["position"].empty_label="...Select the position...."
        self.fields["fullname"].required=False
        self.fields["emp_code"].required=False