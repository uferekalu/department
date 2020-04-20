from django import forms
from .models import Student

class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('fullname','amount','balance','total','mobile','dept')
        labels = {
            'fullname': 'Full Name',
            'amount': 'Amount',
            'balance': 'Balance',
            'total': 'Total',
            'mobile': 'Phone Number',
            'dept': 'Department'
        }
    def __init__(self, *args, **kwargs):
        super(DepartmentForm,self).__init__(*args, **kwargs)
        self.fields['dept'].empty_label = "Select"