from django.shortcuts import render
from django.forms import widgets
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import *
from student.models import *
from management.models import *
from elements.models import *
from attendance.models import *
from .forms import *
import csv
# Create your views here.

def resultpage(request):
    form = CreateResult()
    return render(request,'result.html',context={'form' : form})

def createresult(request):
    if request.method == "POST":
        form = CreateResult(request.POST,request.FILES)
        if form.is_valid():
            ###################################################################
            ############## Fetching and cleaning the data  ####################
            ###################################################################

            year = form.cleaned_data['Year']
            year_name = year
            student = Student.objects.filter(current_year_id=year.id)
            # attendance = Attendance.objects.filter(year_id=year.id)
            # print(student)
            all_marks = []
            all_subject = []
            all_attendance = []
            submited_student = []
            for i,j in enumerate(student):
                # print(i)
                request_roll_year = Student.objects.filter(id=j.id).values()[0]['current_year_id']
                request_roll = Student.objects.filter(id=j.id).values()[0]['Roll_number']
                year = Year.objects.filter(id=request_roll_year)
                try:
                    user = User.objects.filter(username=request_roll).values()[0]['id']
                    submited_student.append(request_roll)
                    # print(submited_student)
                    for i in year:
                        subject = i.subjects.all()
                    assignment = Elements.objects.filter(subject__in=subject)
                    subject_name = []
                    each_attendance = []
                    assignment_marks = [] 
                    marks = []
                    for i in subject:
                        temp = []
                        temp2 = []
                        temp3 = []
                        a = 0
                        # subject_name.append(i.name)
                        all_subject.append(i.name)
                        for j in assignment:
                            if i == j.subject:
                                try:
                                    a = Submissions.objects.filter(assignment_id=j.id,user_id=user).values()
                                    temp.append(Submissions.objects.filter(assignment_id=j.id,user_id=user).values()[0]['grade'])
                                    temp2.append(Elements.objects.filter(id= a[0]['assignment_id']).values()[0]['marks'])
                                    # print(temp)
                                except:
                                    temp.append(0)
                                    pass
                        marks.append(sum(temp))
                        # print(marks)
                        assignment_marks.append(sum(temp2))

                        attendance = Attendance.objects.filter(subject_id=i.id)

                    all_marks.append(marks)
                    # all_subject.append(subject_name)
                    # all_attendance.append(temp3)
                except :

                    ###################################################################
                    ######## if by chances the student username is not created ########
                    ###################################################################
                    # marks = []
                    print(user,'failed')
              

            ####################################################################
            ################### Attendance filteration #########################
            ####################################################################

            for i,j in enumerate(student):
                print(j.id)
                request_roll_year = Student.objects.filter(id=j.id).values()[0]['current_year_id']
                request_roll = Student.objects.filter(id=j.id).values()[0]['Roll_number']
                year = Year.objects.filter(id=request_roll_year)
                all_att = []
                total_att = []
                try:
                    user = User.objects.filter(username=request_roll).values()[0]['id']
                    # submited_student.append(request_roll)
                    for i in year:
                        subject = i.subjects.all()
                    att =[]
                    for k in subject:
                        a = 0
                        b = 0
                        attendance = Attendance.objects.filter(subject_id=k.id)
                        for m,n in enumerate(attendance):
                            b += 1
                            for stu in n.student.all():
                                check = stu.Roll_number
                                if check == request_roll:
                                    # print(check , 'present')
                                    a += 1
                                    # print(a)
                        att.append(a)
                        total_att.append(b)
                    # print(att)
                    all_att.append(att)
                    # print(all_att)
                    # print(total_att)
                except Exception as e:
                    print(e)
                    print('code crahed')
                    # print()
                    pass


            ###############################
            ####### finial print ##########
            ###############################

            print('subjects ',all_subject)
            print('studnet ', submited_student)
            print('student marks ', all_marks)
            print('total marks of each subject ',assignment_marks)
            print('student attendance ',all_att)
            print('total attendance of each subject ',total_att)
            # test(all_subject,submited_student,all_marks,assignment_marks,all_att,total_att,year_name)
            
            ###################################################
            ############### Writing in csv files ##############
            ###################################################

            response = HttpResponse(content_type='text/csv')
            filename = '{}.csv'.format(year_name)
            print(filename)  
            response['Content-Disposition'] = 'attachment; filename={}'.format(filename)  
            writer = csv.writer(response)  

            header = ['Roll Number']
            for i in all_subject:
                header.append(i)
                # header.append('Out off')
            header.append('Total Marks')
            header.append('Out off Marks')

            print(header)
            writer.writerow(header)  

            for i in range(len(submited_student)):
                row_data = []
                total_marks = 0
                row_data.append(submited_student[i])
                for j in range(len(all_subject)):
                    row_data.append(all_marks[i][j])
                    total_marks += all_marks[i][j]
                row_data.append(total_marks) 
                row_data.append(sum(assignment_marks))   

                print(row_data)
                writer.writerow(row_data)  

            return response  
            
            pass

def test(all_subject,submited_student,all_marks,assignment_marks,all_att,total_att,year_name):
    header = ['Roll Number']
    for i in all_subject:
        header.append(i)
        # header.append('Out off')
    print(header)

    for i in range(len(submited_student)):
        row_data = []

        row_data.append(submited_student[i])
        for j in range(len(all_subject)):
            row_data.append(all_marks[i][j])

        
    print('in second funtion')