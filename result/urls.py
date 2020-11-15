from django.urls import path
from . import views

urlpatterns = [
    # path('', admin.site.urls),
    path('',views.resultpage,name='result'),
    path('create/',views.createresult,name='create-result'),
    # path('dashboard/',views.dashboard,name='dashboard'),
    
]