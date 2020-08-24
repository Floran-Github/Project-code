from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from staffs.models import *
from .models import CustomUser
# Create your views here.

def create_staff_user(request):
    i = Staff.objects.all()
    for j in range(len(i)):
        first_name = i.values()[j]['firstname']
        email = first_name+'@gmail.com'

        try:
            user = User.objects.create_user(first_name, email, first_name)  
            user.is_staff=True 
            user.save()
            print('sucess')
        except :
            print('user already created')
    print("hello")
    return HttpResponse('<h1>welcome to first page</h1>')

