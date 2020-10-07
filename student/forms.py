from django import forms
from django.forms import ModelForm, modelformset_factory

from .models import *


class BatchForm(ModelForm):
    number = forms.IntegerField()

    class Meta:
        model = Batch
        fields = ['dept','year']