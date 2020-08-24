from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request,'index.html')

def homepage(request):
    return render(request,'home.html')