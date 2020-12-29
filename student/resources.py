from import_export import resources
from .models import *

class studentResources(resources.ModelResource):
    class Meta:
        model = Student
        exclude = ('id', )