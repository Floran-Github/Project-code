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
from .filters import *
from .forms import *
from management.models import  *

####################################
########### StudentPart ############
####################################

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

####################################
############ BatchPart #############
####################################

class BatchListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
  model = Batch
  template_name = 'student/batchs_list.html'

  def get_context_data(self, **kwargs):
      year_list = Year.objects.all().order_by('name')
      dept_list = Department.objects.all()
      batch_list = Batch.objects.all()
      sorted_year_list = []
      sorted_dept_list = []
      sorted_year_list_name = []
      sorted_dept_list_name = []
      
      for i in batch_list:
            sorted_year_list.append(i.year)
            sorted_year_list_name.append(i.year.name)
            sorted_dept_list.append(i.dept)
            sorted_dept_list_name.append(i.dept.name)

      sorted_year_list = set(sorted_year_list)
      sorted_dept_list = set(sorted_dept_list)

      a = set()
      b = [x for x in sorted_year_list_name if not (x in a or a.add(x))]
      b.sort()          
      sorted_dept_list_name = set(sorted_dept_list_name)

      context = super().get_context_data(**kwargs)
      context['form'] = BatchForm()
      context['years'] = sorted_year_list
      context['depts'] = sorted_dept_list
      context['years_name'] = b
      context['depts_name'] = sorted_dept_list_name
      return context

@login_required
def BatchCreate(request):
    if request.method == 'POST':
        form = BatchForm(request.POST, request.FILES)

        if form.is_valid():
            a = form.cleaned_data['number']
            b = form.cleaned_data['year']
            c = form.cleaned_data['dept']

            student = Student.objects.filter(current_year_id = b,current_dept_id = c)
            no_batch = int(len(student)/a)
            if no_batch >= 1:
                student_divide = [student[i:i+no_batch] for i in range(0,len(student),no_batch)]
                
                for i,j in enumerate(student_divide):
                    try:
                        batch_name = 'Batch - {}'.format(i+1)
                        batch = Batch(batch_no=batch_name,dept=c,year=b)
                        batch.save()
                        batch_add = Batch.objects.get(batch_no=batch_name,dept=c,year=b)
                        batch_add.student.add(*j)
                    except:
                        messages.error(request,'Batch already exists')
                        break
            else:
                messages.error(request,'Number of batch should not be more than the number of student')
                
            return redirect('batch')
  
class BatchStudentListView(ListView):
    model = Batch
    template_name = 'student/batch_list.html'

    def get_queryset(self,*args, **kwargs):
        pass
      
    def get_context_data(self,**kwargs):

        context = super(BatchStudentListView, self).get_context_data(**kwargs)
        context['form'] = Batch.objects.filter(pk=self.kwargs.get('pk'))

        return context
        
class BatchDeleteView(LoginRequiredMixin, DeleteView):
    model = Batch
    success_url = reverse_lazy('batch')
