from django.db import models

# Create your models here.
class  Department(models.Model):
    ''' Department '''
    name = models.CharField(max_length=200,unique= True)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        ordering = ['name']

    def __str__(self):
        return self.name

    
class Year(models.Model):
    ''' Year '''

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    ''' Year '''

    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name

