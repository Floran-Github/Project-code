from django.shortcuts import render
# Create your views here.
from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from student.models import *
from staffs.models import *
from .models import *
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy
# Create your views here.

class StudentuserListView(ListView):
    model = studentUser

def create_student(request):
    a,b = 0,0
    i = Student.objects.all()
    print(len(i))
    for j in range(len(i)):
        print(j)
        Roll_name = i.values()[j]['Roll_number']
        password = i.values()[j]['Roll_number']
        email = Roll_name+'@gmail.com'
        studentId = Student.objects.get(Roll_number = Roll_name)
    
    # if User.objects.filter(username=cleaned_data[first_name]).exists():
        try:
            user = User.objects.create_user(Roll_name, email, password)  
            user.is_staff=False 
            user.save()

            student_user_create = studentUser.objects.create(user = user , student_id =studentId)
            print('sucess')
            a += 1
        except :
            b += 1
            print('user already created')
            continue
    context ={
        'newUser' : a,
        'duplicateUser' : b,
    }
    return render(request,'create_users/create.html',context=context)




class TeacheruserListView(ListView):
    model = teacherUser

def create_teacher(request):
    a,b = 0,0
    i = Staff.objects.all()
    print(len(i))
    for j in range(len(i)):
        print(j)
        surname = i.values()[j]['surname']
        firstName = i.values()[j]['firstname']
        password = i.values()[j]['firstname']
        userName = firstName+'.'+surname
        email = userName +'@gmail.com'
        staffId = Staff.objects.get(firstname = firstName)
        try:
            user = User.objects.create_user(userName, email, password)  
            user.is_staff=True 
            user.save()

            teacher_user_create = teacherUser.objects.create(user = user , teacher_id =staffId)
            print('sucess')
            a += 1
        except :
            b += 1
            print('user already created')
            continue
    context ={
        'newUser' : a,
        'duplicateUser' : b,
    }
    return render(request,'create_users/createTeacher.html',context=context)


