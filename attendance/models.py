from django.db import models
from management.models import *
from student.models import *
from django.contrib.auth.models import User

# Create your models here.
class Attendance(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE, blank=False,null=False)
    year = models.ForeignKey(Year,on_delete=models.CASCADE, blank=False,null=False)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE, blank=False,null=False)
    student = models.ManyToManyField(Student)
    teacher = models.CharField(max_length=200)

    
    def __str__(self):
        return f'{self.subject} {self.name}'  