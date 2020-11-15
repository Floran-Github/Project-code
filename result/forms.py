from django import forms
# from student.models import *
from management.models import *

class CreateResult(forms.Form):
    Year = forms.ModelChoiceField(queryset=Year.objects.all())
    
    