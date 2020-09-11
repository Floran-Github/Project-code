from django.db import models
from management.models import *
from django.contrib.auth.models import User

# Create your models here.

class Elements(models.Model):
    STATUS =[
        ('experiment', 'Experiment'),
        ('assignment', 'Assignment'),
        ('mini project','Mini Project'),
    ]

    elements_status = models.CharField(max_length=15, choices = STATUS,default='experiment')

    element_name = models.CharField(max_length = 50)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)

    marks = models.IntegerField()

    upload = models.FileField(upload_to='assignments/')

    due_date = models.DateField()
    created_date = models.DateField(auto_now=True)
    last_update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.element_name
    
    def get_absolute_url(self):
        return reverse('element-detail',kwargs={'pk': self.pk})


class Submissions(models.Model):

    STATUS = [
      ('unsubmitted', 'Unsubmitted'),
      ('submitted', 'Submitted'),
     
  ]

    submission_status  = models.CharField(max_length=15, choices=STATUS, default='unsubmitted')

    upload = models.FileField(upload_to='submissions/')
    submitted_at = models.DateField(auto_now=True)

    assignment = models.ForeignKey(Elements,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    grade = models.IntegerField(default=0)
    feedback = models.CharField(max_length=255, null=True, blank=True, default="No feedback yet")

    def __str__(self):
        return f'Submitted by {self.user}'

    def get_absolute_url(self):
        return reverse('submission-detail', kwargs={'pk': self.pk})