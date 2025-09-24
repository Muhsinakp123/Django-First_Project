from django.shortcuts import get_object_or_404, redirect, render

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
def testing(request):
    fruits = ['apple','Banana','Cherry','orange']
    return render(request,'template.html',{'fruits': fruits})
def add (request):
    return render(request,'add.html')
def addmember(request):
        x = request.POST["firstname"]
        y = request.POST["lastname"]
        z = request.POST['phone']
        j = request.POST['joined_date']
        
        
        # Save new member
        new_memeber = App(firstname=x, lastname=y, phone=z, joined_date=j)
        
        new_memeber.save()
        
        return redirect("sample")
    
def update (request,id):
    m = App.objects.get(id=id)
    return render(request, "update.html", {"mymember": m})


    
def update_member(request,id):
        updated =  App.objects.get(id=id)
        updated.firstname = request.POST["firstname"]
        updated.lastname = request.POST["lastname"]
        updated.phone = request.POST["phone"]
        updated.joined_date = request.POST["joined_date"]
        updated.save()
        
        return redirect("sample")
    
def delete_member(request, id):
    dele =  App.objects.get(id=id)         # fetch member by id
    dele.delete()                          # delete from DB
    return redirect("sample")