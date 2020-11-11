from django.urls import path

from .views import *

urlpatterns = [
  path('list/', AttendanceList.as_view(), name='attendance'),
  path('create/',createAttendance,name='create-attendance'),
  path('year/<int:pk>/update/',UpdateAttenadance.as_view(), name='attendance-update'),
  path('year/<int:pk>/delete/',DeleteAttendance.as_view(), name='attendance-delete'),
  
]