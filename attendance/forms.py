from django import forms
from django.forms import ModelForm, modelformset_factory

from .models import *


class AttendanceForm(ModelForm):
    absent_rollnumber = forms.CharField()

    class Meta:
        model = Attendance
        fields = ['name','dept','year','subject']

        # def __init__(self, user, *args, **kwargs):
        #     super(AttendanceForm, self).__init__(*args, **kwargs)
            
        #     self.fields['subject'].queryset = Subject.objects.filter(teacher=Staff.objects.filter(firstname=user))



class AttendanceUpdate(ModelForm):
    class Meta:
        model = Attendance
        fields = fields = ['name','dept','year','subject','student']
        widgets = {
                'student': forms.CheckboxSelectMultiple,
            }
