from django.urls import path

from . import views

urlpatterns = [
    path('',views.StudentuserListView.as_view(),name='create'),
    path('create',views.create_student,name='create-user'),
    path('teacher',views.TeacheruserListView.as_view(),name='create-teacher'),
    path('create-teacher',views.create_teacher,name='create-teacher-user'),
]