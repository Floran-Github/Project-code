from django.urls import path
from . import views



urlpatterns = [
    # path('', admin.site.urls),
    path('',views.mainpage,name='mainpage'),
    path('homepage/',views.dashboard,name='homepage'),
    
    
]
