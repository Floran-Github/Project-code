from django import forms
from django.forms import ModelForm, modelformset_factory

from .models import *

class DepartmentForm(ModelForm):
  prefix = 'Class'
  class Meta:
    model = Department
    fields = ['name']

class YearForm(ModelForm):
  prefix = 'Class'
  class Meta:
    model = Year
    fields = ['name']

class SubjectForm(ModelForm):
  prefix = 'Subject'
  class Meta:
    model = Subject
    fields = ['name','Coursecode']
