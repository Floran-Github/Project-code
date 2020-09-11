from django import forms
from django.forms import ModelForm, modelformset_factory

from .models import *


class SubmissionForm(ModelForm):
    upload = forms.FileField(required=True)

    class Meta:
        model = Submissions
        fields = ['upload']