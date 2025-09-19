from django.shortcuts import render

from .models import App

# Create your views here.

def index (request):
    return render(request,'main.html')
def sample (request):
    # return render(request,'sample.html')
     mymembers = App.objects.all().values()
     return render(request,'sample.html',{'mymembers': mymembers})
def details (request,id):
     mymembers = App.objects.get(id=id)
     return render(request,'details.html',{'mymember': mymembers})