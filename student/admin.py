from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import *
# Register your models here.

@admin.register(Student)
class student(ImportExportModelAdmin):
    pass

admin.site.register(Batch)
