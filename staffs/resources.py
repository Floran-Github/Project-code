from import_export import resources
from .models import *

class staffResources(resources.ModelResource):
    class Meta:
        model = Staff
        exclude = ('id')