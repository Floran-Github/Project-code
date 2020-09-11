from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import *
from .forms import *



from django.shortcuts import render

# Create your views here.
@login_required
def index_view(request):
  return render(request, 'home.html')
############### DEPARTMENT ################################

class DeptListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
  model = Department
  template_name = 'management/dept_list.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['form'] = DepartmentForm()
      return context



class DeptCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  form_class = DepartmentForm
  template_name = 'management/mgt_form.html'
  success_url = reverse_lazy('Department')
  success_message = 'New class successfully added'



class DeptUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
  model = Department
  fields = ['name']
  success_url = reverse_lazy('Department')
  success_message = 'class successfully updated.'
  template_name = 'management/mgt_form.html'



class DeptDeleteView(LoginRequiredMixin, DeleteView):
  model = Department
  success_url = reverse_lazy('Department')
  template_name = 'management/core_confirm_delete.html'
  success_message = "The class {} has been deleted with all its attached content"


  def delete(self, request, *args, **kwargs):
      obj = self.get_object()
      print(obj.name)
      messages.success(self.request, self.success_message.format(obj.name))
      return super(DeptDeleteView, self).delete(request, *args, **kwargs)

############### YEAR ##################################

class YearListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
  model = Year
  template_name = 'management/year_list.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['form'] = YearForm()
      return context



class YearCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  form_class = YearForm
  template_name = 'management/year.html'
  success_url = reverse_lazy('Year')
  success_message = 'New class successfully added'



class YearUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
  model = Year
  form_class = YearForm
  success_url = reverse_lazy('Year')
  success_message = 'class successfully updated.'
  template_name = 'management/year.html'



class YearDeleteView(LoginRequiredMixin, DeleteView):
  model = Year
  success_url = reverse_lazy('Year')
  template_name = 'management/core_confirm_delete.html'
  success_message = "The class {} has been deleted with all its attached content"


  def delete(self, request, *args, **kwargs):
      obj = self.get_object()
      print(obj.name)
      messages.success(self.request, self.success_message.format(obj.name))
      return super(YearDeleteView, self).delete(request, *args, **kwargs)

#subject


class SubjectListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
  model = Subject
  template_name = 'management/subject_list.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['form'] = SubjectForm()
      return context



class SubjectCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  form_class = SubjectForm
  template_name = 'management/mgt_form.html'
  success_url = reverse_lazy('subjects')
  success_message = 'New subject successfully added'



class SubjectUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
  model = Subject
  fields = ['name']
  success_url = reverse_lazy('subjects')
  success_message = 'Subject successfully updated.'
  template_name = 'management/mgt_form.html'



class SubjectDeleteView(LoginRequiredMixin, DeleteView):
  model = Subject
  success_url = reverse_lazy('subjects')
  template_name = 'management/core_confirm_delete.html'
  success_message = "The subject {} has been deleted with all its attached content"

  def delete(self, request, *args, **kwargs):
      obj = self.get_object()
      messages.success(self.request, self.success_message.format(obj.name))
      return super(SubjectDeleteView, self).delete(request, *args, **kwargs)
