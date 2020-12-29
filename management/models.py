from django.db import models
from django.contrib.postgres.fields import *
from staffs.models import *
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class  Department(models.Model):
    ''' Department '''
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        # ordering = ['name']

    def __str__(self):
        return self.name

class Subject(models.Model):
    ''' Subject '''

    name = models.CharField(max_length=50, unique=True)
    Coursecode = models.CharField(max_length=50, null = True)
    teacher = models.ForeignKey(Staff,on_delete=models.SET_NULL, blank=True, null=True)

    # class Meta:
    #     ordering = ['name']
        
    def __str__(self):
        return self.name

class Year(models.Model):
    ''' Year '''

    name = models.CharField(max_length=50, unique=True)
    dept = models.ForeignKey(Department,on_delete=models.SET_NULL,null = True,blank=True)
    subjects = models.ManyToManyField(Subject)
    def __str__(self):
        return f'{self.name}{self.dept}'




