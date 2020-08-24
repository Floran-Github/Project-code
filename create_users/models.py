from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from student.models import Student
class CustomUser(User):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
# Create your models here.
