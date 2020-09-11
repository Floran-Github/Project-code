from django.shortcuts import render

# Create your views here.
import csv
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy

from .models import Student, StudentBulkUpload
from .filters import *

# from finance.models import Invoice

# @login_required
# def student_list(request):
#   students = Student.objects.all()
#   return render(request, 'students/student_list.html', {"students":students})


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = "student/student_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = StudentFilter(self.request.GET,queryset = self.get_queryset())
        return context


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = "student/student_detail.html"

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        # context['payments'] = Invoice.objects.filter(student=self.object)
        return context


class StudentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Student
    fields = '__all__'
    success_message = "New student successfully added."

    def get_form(self):
        '''add date picker in forms'''
        form = super(StudentCreateView, self).get_form()
        form.fields['date_of_birth'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 2})
        
        return form


class StudentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Student
    fields = '__all__'
    success_message = "Record successfully updated."

    def get_form(self):
        '''add date picker in forms'''
        form = super(StudentUpdateView, self).get_form()
        form.fields['date_of_birth'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        form.fields['date_of_admission'].widget = widgets.DateInput(attrs={
                                                                    'type': 'date'})
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 2})
        
        form.fields['profile_pic'].widget = widgets.FileInput()
        return form


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('student-list')


class StudentBulkUploadView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = StudentBulkUpload
    template_name = 'student/students_upload.html'
    fields = ['csv_file']
    success_url = '/student/list'
    success_message = 'Successfully uploaded students'

@login_required
def downloadcsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="student_template.csv"'

    writer = csv.writer(response)
    writer.writerow(['Gr_number',
                    'surname',
                     'firstname',
                     'Roll_number', 
                     'gender', 
                     'Father_Name',
                     'Mother_Name', 
                     'address',
                     'date_of_birth',
                     'date_of_admission',
                     'current_year',
                     'current_dept',
                     'parent_mobile_number'])

    return response