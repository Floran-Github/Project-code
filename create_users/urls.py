from django.urls import path

from . import views

urlpatterns = [
    path('',views.StudentuserListView.as_view(),name='create'),
    path('create',views.create_student,name='create-user'),
]