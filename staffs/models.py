from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import RegexValidator
from management.models import *

class Staff(models.Model):
  STATUS = [
      ('assistant', 'Assistant'),
      ('lecturer', 'Lecturer')
  ]

  GENDER = [
      ('male', 'Male'),
      ('female', 'Female')
  ]

  current_status      = models.CharField(max_length=10, choices=STATUS, default='assistant')
  staff_id_number     = models.IntegerField() 

  surname             = models.CharField(max_length=200)
  firstname           = models.CharField(max_length=200)
  
  # Subject             = models.ForeignKey(Subject, on_delete=models.SET_NULL, blank=True, null=True)

  gender              = models.CharField(max_length=10, choices=GENDER, default='male')
  date_of_birth       = models.DateField(default=timezone.now)

  date_of_join   = models.DateField(default=timezone.now)

  mobile_num_regex    = RegexValidator(regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!")
  mobile_number       = models.CharField(validators=[mobile_num_regex], max_length=13, blank=True)
  
  address             = models.TextField(blank=True)
  

  def __str__(self):
    return f'{self.surname} {self.firstname}'

  def get_absolute_url(self):
    return reverse('staff-detail', kwargs={'pk': self.pk})


class Head(models.Model):
  STATUS = [
      ('head', 'Head'),
      ('dean', 'Dean'),
      ('director', 'Director'),
  ]

  GENDER = [
      ('male', 'Male'),
      ('female', 'Female')
  ]

  surname             = models.CharField(max_length=200)
  firstname           = models.CharField(max_length=200)

  # department          = models.ForeignKey(Department,on_delete=models.CASCADE)
  title               = models.CharField(max_length=10, choices=STATUS, default='head')

  gender              = models.CharField(max_length=10, choices=GENDER, default='male')

  fromDate            = models.DateField(default=timezone.now)
  toDate              = models.DateField(default=timezone.now)

  def __str__(self):
    return f'{self.surname} {self.firstname}'

  def get_absolute_url(self):
    return reverse('head-detail', kwargs={'pk': self.pk})