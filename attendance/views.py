from django.shortcuts import render
import csv
from django.http import HttpResponse
from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Student, StudentBulkUpload
from .forms import *
from management.models import  *
from staffs.models import  *

####################################
######### Attendence Part ##########
####################################

class AttendanceList(ListView):
    template_name = 'attendance/att_list.html'
    def get_queryset(self):
        if self.request.user.is_superuser:
            self.show_att = Attendance.objects.all()         
        else:
        ######## Filtering part########
            self.show_att = Attendance.objects.filter(teacher=str(self.request.user.username))
        
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['form'] = AttendanceForm()
        context['attendance_lists'] = self.show_att
        return context

def createAttendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            dept = form.cleaned_data['dept']
            year = form.cleaned_data['year']
            subject = form.cleaned_data['subject']
            absent_rollnumber = form.cleaned_data['absent_rollnumber']
            student = Student.objects.filter(current_year_id = year,current_dept_id = dept)
            absent = absent_rollnumber.split(',')
            for i,j in enumerate(student):
                try:
                    roll_number = student.values()[i]['Roll_number']
                    if roll_number in absent:
                        pass
                    else:
                        att = Attendance(name=name,dept=dept,year=year,subject=subject,teacher=str(request.user.username))
                        att.save()
                        att_add = Attendance.objects.get(name=name,dept=dept,year=year,subject=subject,teacher=str(request.user.username))
                        att_add.student.add(j)
                except Exception as e:
                    messages.error(request,'Error Occur During Creating Attendance, Try Again !')
                    break

        return redirect('attendance')

class UpdateAttenadance(UpdateView):
    model = Attendance
    form_class = AttendanceUpdate
    success_url = reverse_lazy('attendance')
    success_message = 'Attendance successfully updated.'
    template_name = 'attendance/update_attendance.html'
    
class DeleteAttendance(DeleteView):
    model = Attendance
    success_url = reverse_lazy('attendance')
    template_name = 'attendance/core_confirm_delete.html'
    success_message = "The class {} has been deleted with all its attached content"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        print(obj.name)
        messages.success(self.request, self.success_message.format(obj.name))
        return super(DeleteAttendance, self).delete(request, *args, **kwargs)