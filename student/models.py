from django.db import models
from django.utils import timezone
from django.urls import reverse


from management.models import *
from django.core.validators import RegexValidator




class Student(models.Model):
  STATUS = [
      ('active', 'Active'),
      ('inactive', 'Inactive')
  ]

  GENDER = [
      ('male', 'Male'),
      ('female', 'Female')
  ]

  current_status        = models.CharField(max_length=10, choices=STATUS, default='active')
  Gr_number             = models.CharField(max_length=200, unique=True)
  
  surname               = models.CharField(max_length=200)
  firstname             = models.CharField(max_length=200)
  
  Roll_number             = models.CharField(max_length=200, unique=True)

  Father_Name           = models.CharField(max_length=200)
  Mother_Name           = models.CharField(max_length=200)

  gender                = models.CharField(max_length=10, choices=GENDER, default='male')
  date_of_birth         = models.DateField(default=timezone.now)
  date_of_admission     = models.DateField(default=timezone.now)

  current_year         = models.ForeignKey(Year, on_delete=models.SET_NULL, blank=True, null=True)
  current_dept         = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)

  mobile_num_regex      = RegexValidator(regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!")
  parent_mobile_number  = models.CharField(validators=[mobile_num_regex], max_length=13, blank=True)

  address               = models.TextField(blank=True)
  
  profile_pic           = models.ImageField(blank=True, upload_to='students/pic/')  

  class Meta:
    ordering = ['Gr_number','Roll_number']

  def __str__(self):
    return f'{self.surname} {self.firstname} '

  def get_absolute_url(self):
    return reverse('student-detail', kwargs={'pk': self.pk})


class StudentBulkUpload(models.Model):
  date_uploaded       = models.DateTimeField(auto_now=True)
  csv_file            = models.FileField(upload_to='students/bulkupload/')

