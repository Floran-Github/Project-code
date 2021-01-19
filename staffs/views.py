from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy
from .models import Staff,Head
from .resources import *
from datetime import datetime
import csv
from tablib import Dataset
####################################
############ StaffPart #############
####################################

class StaffListView(ListView):
    model = Staff

class StaffDetailView(DetailView):
    model = Staff
    template_name = "staffs/staff_detail.html"

class StaffCreateView(SuccessMessageMixin, CreateView):
    model = Staff
    fields = '__all__'
    success_message = 'New staff successfully added'

    def get_form(self):
        '''add date picker in forms'''
        form = super(StaffCreateView, self).get_form()
        form.fields['date_of_birth'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        form.fields['date_of_join'].widget = widgets.DateInput(attrs={
                                                                    'type': 'date'})
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        
        return form

class StaffUpdateView(SuccessMessageMixin, UpdateView):
    model = Staff
    fields = '__all__'
    success_message = "Record successfully updated."

    def get_form(self):
        '''add date picker in forms'''
        form = super(StaffUpdateView, self).get_form()
        form.fields['date_of_birth'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        form.fields['date_of_join'].widget = widgets.DateInput(attrs={
                                                                    'type': 'date'})
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        
        return form

class StaffDeleteView(DeleteView):
  model = Staff
  success_url = reverse_lazy('staff-list')

@login_required
def bulkUpload(request):
    student_resources = staffResources()
    dataset = student_resources.export()

    # exporting file here
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="staff-data.csv"'
    return response  
    
@login_required
def downloadcsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="staff_data_to_be_import.csv"'

    writer = csv.writer(response)
    writer.writerow(['current_status',
                    'staff_id_number',
                     'surname',
                     'firstname', 
                     'gender',
                     'date_of_birth',
                     'date_of_join',
                     'mobile_number',
                     'address',
                     ])

    return response
    
@login_required  
def csv_to_staff_database(request):
    if request.method == 'POST':
        staff_resource = staffResources()
        dataset = Dataset()
        new_employees = request.FILES['importstaffData']
        imported_data = dataset.load(new_employees.read().decode('utf-8'),format='csv')
        
        data = [
            Staff(
                current_status = i[0],
                staff_id_number = i[1],
                surname = i[2],
                firstname = i[3],
                gender = i[4],
                date_of_birth = datetime.strptime(i[5],'%m/%d/%Y').strftime('%Y-%m-%d'),
                date_of_join = datetime.strptime(i[6],'%m/%d/%Y').strftime('%Y-%m-%d'),
                mobile_number = i[7],
                address = i[8],
            ) for i in imported_data 
        ]

        print(len(data))

        Staff.objects.bulk_create(objs=data)
        return redirect('staff-list')

    return render(request, 'staffs/import_sims.html')  
    
####################################
##### Head of Department Part ######
####################################

class HeadListView(ListView):
    model = Head

class HeadDetailView(DetailView):
    model = Head
    template_name = "staffs/head_detail.html"

class HeadCreateView(SuccessMessageMixin, CreateView):
    model = Head
    fields = '__all__'
    success_message = 'New Head successfully added'

    def get_form(self):
        '''add date picker in forms'''
        form = super(HeadCreateView, self).get_form()
        form.fields['fromDate'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        form.fields['toDate'].widget = widgets.DateInput(attrs={
                                                                    'type': 'date'})
        
        return form

class HeadUpdateView(SuccessMessageMixin, UpdateView):
    model = Head
    fields = '__all__'
    success_message = "Record successfully updated."

    def get_form(self):
        '''add date picker in forms'''
        form = super(HeadUpdateView, self).get_form()
        form.fields['fromDate'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        form.fields['toDate'].widget = widgets.DateInput(attrs={
                                                                    'type': 'date'})
        
        return form

class HeadDeleteView(DeleteView):
  model = Head
  success_url = reverse_lazy('head-list')
