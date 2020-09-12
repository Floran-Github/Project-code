from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from student.models import Student
from staffs.models import Staff

class studentUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)

    def __str__(self):
       return f'{self.user.username}'

class teacherUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Staff,on_delete=models.CASCADE)

    def __str__(self):
       return f'{self.user.username}'