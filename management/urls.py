from django.urls import path

from . import views

urlpatterns = [
  path('', views.index_view, name='home'),
  path('Department/list/', views.DeptListView.as_view(), name='Department'),
  path('Department/create/', views.DeptCreateView.as_view(), name='Department-create'),
  path('Department/<int:pk>/update/',
       views.DeptUpdateView.as_view(), name='Department-update'),
  path('Department/<int:pk>/delete/',
       views.DeptDeleteView.as_view(), name='Department-delete'),

  path('year/list/', views.YearListView.as_view(), name='Year'),
  path('year/create/', views.YearCreateView.as_view(), name='Year-create'),
  path('year/<int:pk>/update/',
       views.YearUpdateView.as_view(), name='Year-update'),
  path('year/<int:pk>/delete/',
       views.YearDeleteView.as_view(), name='Year-delete'),

  path('subject/list/', views.SubjectListView.as_view(), name='subjects'),
  path('subject/create/', views.SubjectCreateView.as_view(),
       name='subject-create'),
  path('subject/<int:pk>/update/',
       views.SubjectUpdateView.as_view(), name='subject-update'),
  path('subject/<int:pk>/delete/',
       views.SubjectDeleteView.as_view(), name='subject-delete'),

]
