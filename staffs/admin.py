from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import  *
@admin.register(Staff)
class staff(ImportExportModelAdmin):
    list_display=['current_status',
                    'staff_id_number',
                     'surname',
                     'firstname', 
                     'gender',
                     'date_of_birth',
                     'date_of_join',
                     'mobile_number',
                     'address',]
    pass
@admin.register(Head)
class head(ImportExportModelAdmin):
    pass