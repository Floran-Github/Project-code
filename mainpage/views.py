from django.shortcuts import render
from django.views.defaults import page_not_found
from elements.models import *   ### change it to element
from student.models import *
from attendance.models import *
# Create your views here.



def mainpage(request):
    return render(request,'index.html')


##dashboard
def homepage(request):
    return render(request,'home.html')

def dashboard(request):

    if request.user.is_superuser:
        subjects = Subject.objects.all()

        attendance = Attendance.objects.filter(subject__in= subjects)

        number_of_student = []
        subject = []
        subject_name = []
        attendance_label = []
        for i in subjects:
            temp = []
            temp2 = []
            subject.append(i)
            subject_name.append(i.name)
            for j in attendance:
                if i == j.subject:
                    temp2.append(j.name)
                    temp.append(j.student.count())
            number_of_student.append(temp)
            attendance_label.append(temp2)

        cleaned_data = [ele for ele in number_of_student if ele != []]

        print(subject_name)
        print(number_of_student)
        print(cleaned_data)
        print(attendance_label)

        context={
            'number' : range(len(subject)),
            'label'  : attendance_label,
            'data'   : number_of_student,
            'subject': subject_name,
            'a'      : len(subject),
        }
        return render(request,'dashboard_staff.html',context=context)
        pass

    elif request.user.is_staff and not request.user.is_superuser:
        username = request.user.username
        username = username.split(".")

        teacher = Staff.objects.filter(firstname = username[0]).values()[0]['id']
        teacher_subject = Subject.objects.filter(teacher_id = teacher)

        attendance = Attendance.objects.filter(subject__in= teacher_subject)

        number_of_student = []
        subject = []
        subject_name = []
        
        attendance_label = []
        for i in teacher_subject:
            temp = []
            temp2 = []
            subject.append(i)
            subject_name.append(i.name)
            for j in attendance:
                if i == j.subject:
                    temp2.append(j.name)
                    temp.append(j.student.count())
            number_of_student.append(temp)
            attendance_label.append(temp2)

        cleaned_data = [ele for ele in number_of_student if ele != []]

        print(subject_name)
        print(cleaned_data)
        print(attendance_label)

        context={
            'number' : range(len(subject)),
            'label'  : attendance_label,
            'data'   : cleaned_data,
            'subject': subject_name,
            'a'      : len(subject)
        }

        return render(request,'dashboard_staff.html',context=context)

    else:
        roll_number = request.user.username
        request_roll_year = Student.objects.filter(Roll_number=roll_number).values()[0]['current_year_id']
        
        year = Year.objects.filter(id=request_roll_year)
        
        for i in year:
                subject = i.subjects.all()

        assignment = Elements.objects.filter(subject__in=subject)
        print(assignment)
        submission = Submissions.objects.filter(user=request.user)
        subject_name = []
        assignment_name = []
        marks = []

        for i in subject:
            temp = []
            temp2 = []
            subject_name.append(i.name)
            for j in assignment:
                if i == j.subject:
                    print('yo')
                    try:
                        print('yoyoy34')
                        a = Submissions.objects.filter(assignment_id=j.id,user_id=2).values()
                        temp.append(Submissions.objects.filter(assignment_id=j.id,user=request.user).values()[0]['grade'])

                        print(Elements.objects.filter(id= a[0]['assignment_id']).values()[0]['element_name'])
                        temp2.append(Elements.objects.filter(id= a[0]['assignment_id']).values()[0]['element_name'])
                        
                    except:
                        pass
            marks.append(temp)
            assignment_name.append(temp2)

        subject_len = len(subject_name)
        print(subject_name)
        print(assignment_name)
        print(marks)
        print(subject_len)
    
        context = {
            'number' : range(subject_len),
            'label'  : assignment_name,
            'subject' : subject_name,
            'data'   : marks,
            'a' : subject_len
        }

        return render(request,'dashboard.html',context=context)


