from django.shortcuts import render

# Create your views here.
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy
from datetime import *
from .models import *
from .forms import *
from django.contrib import messages
from student.models import *
from management.models import *
from django.db.models import Q


class ElementListView(ListView):
    model = Elements
    


class ElementDetailView(DetailView):
    model = Elements
    template_name = "elements/element_detail.html"


class ElementCreateView(SuccessMessageMixin, CreateView):
    model = Elements
    fields = '__all__'
    success_message = 'New element successfully added'

    def get_form(self):
        '''add date picker in forms'''
        form = super(ElementCreateView, self).get_form()
        form.fields['due_date'].widget = widgets.DateInput(
            attrs={'type': 'date'})
    
        return form


class ElementUpdateView(SuccessMessageMixin, UpdateView):
    model = Elements
    fields = '__all__'
    success_message = "Record successfully updated."

    def get_form(self):
        '''add date picker in forms'''
        form = super(ElementUpdateView, self).get_form()
        form.fields['due_date'].widget = widgets.DateInput(
            attrs={'type': 'date'})
       
        return form

class ElementDeleteView(DeleteView):
  model = Elements
  success_url = reverse_lazy('element-list')


################################### STUDENT PART #######################################
class SubmissionListView(ListView):
    # model = Elements
    template_name = 'elements\submission_list.html'

    def get_queryset(self):
        if self.request.user.is_superuser:

            self.year = Year.objects.all()
            self.submissions = Submissions.objects.all()
            
            self.element = Elements.objects.all()
            self.submitted = []
            self.submitted_subject = []
            self.pending_subject = []
            for i in self.element:
                    for j in self.submissions:
                        if i == j.assignment:
                            self.submitted.append(i)
                            self.submitted_subject.append(i.subject)
                     
            self.element2 = Elements.objects.exclude(Q(submissions__isnull=False))             
            for i in self.element2:
                self.pending_subject.append(i.subject)
           
            print(set(self.submitted_subject))
            print(set(self.pending_subject))
            print(self.submitted)
            print(self.element)


        else:
            self.student_year = Student.objects.filter(Roll_number=self.request.user.username).values()[0]['current_year_id']
            self.year = Year.objects.filter(pk=self.student_year)
            
            
            print(len(self.year))
            for i in self.year:
                self.a = i.subjects.all()

            print(self.a)
            
            self.submissions = Submissions.objects.filter(user=self.request.user)
            self.element = Elements.objects.filter(subject__in=self.a)
            self.submitted = []
            self.submitted_subject = []
            self.pending_subject = []
            for i in self.element:
                    for j in self.submissions:
                        if i == j.assignment:
                            self.submitted.append(i)
                            self.submitted_subject.append(i.subject)
                     
            self.element2 = Elements.objects.filter(subject__in=self.a).exclude(Q(submissions__isnull=False))             
            for i in self.element2:
                self.pending_subject.append(i.subject)
           
            print(set(self.submitted_subject))
            print(set(self.pending_subject))
            print(self.submitted)
            print(self.element)

    def get_context_data(self, **kwargs):
        context = super(SubmissionListView, self).get_context_data(**kwargs)
        
        context['test'] = set(self.pending_subject)
        context['test2'] = set(self.submitted_subject)
        context['sub'] = self.submitted
        context['ped'] = self.element2
       
        return context



class SubmissionCreateView(SuccessMessageMixin,CreateView):
    model = Submissions
    fields = {'upload'}
    success_message = 'You have submitted assignment'
    template_name = 'elements\submission_form.html'
    

    def form_valid(self, form):
        form.instance.assignment = Elements.objects.get(pk=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.submission_status = 'submitted'
        return super(SubmissionCreateView, self).form_valid(form)

class SubmissionUpdateView(SuccessMessageMixin, UpdateView):
    model = Submissions
    fields = {'upload'}
    success_message = 'You have updated assignment'
    template_name = 'elements\submission_form.html'
    

    def form_valid(self, form):
        form.instance.assignment = Elements.objects.get(pk=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.submission_status = 'submitted'
        return super(SubmissionCreateView, self).form_valid(form)


class SubmissionDetailView(DetailView):
    model = Elements
    template_name = "elements/submission_detail.html"  


############################ TEACHER PART ##############################################

class SubimittedListView(ListView):
    # model = Submissions
    template_name = 'elements/submited_list.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            self.teacher_subject = Subject.objects.all()
            self.submit = Elements.objects.filter(subject__in=self.teacher_subject)

            pass
        else:
            username = self.request.user.username
            username = username.split(".")

            self.teacher = Staff.objects.filter(firstname = username[0]).values()[0]['id']
            self.teacher_subject = Subject.objects.filter(teacher_id = self.teacher)

            print(self.teacher_subject)

            self.submit = Elements.objects.filter(subject__in=self.teacher_subject)

            print(self.submit)
            print(Submissions.objects.filter(assignment__in = self.submit))
            self.a =[]
            for i in self.submit:
                self.a.append(i.subject)

            print(self.a)
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SubimittedListView , self).get_context_data(**kwargs)
        
        context['test'] = Submissions.objects.filter(assignment__in = self.submit)
        context['subject'] = self.teacher_subject
        context['element_id'] = self.submit

        return context


class GradeView(SuccessMessageMixin, UpdateView):
    model = Submissions
    fields = {'grade'}
    success_message = "Record successfully updated."
    template_name = 'elements\grade.html'
    success_url = reverse_lazy('submit-list')

