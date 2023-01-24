from django.shortcuts import render
from django.http import HttpResponse

from .forms import Bookingform
from .models import Department,Doctors

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def booking(request):

    if request.method=='POST':
        form = Bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'conformation.html')

    form = Bookingform()
    dict_form={
        'form':form
    }
    return render(request,'booking.html', dict_form)

def doctors(request):
    dict_doc={
        'doct':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_doc)

def department(request):
    dict_dpt={
        'dict':Department.objects.all()
    }
    return render(request,'department.html',dict_dpt)

def contact(request):
    return render(request,'contact.html')

def search(request):
    if request.method=="POST":
        r=request.POST['r']
        doc=Doctors.objects.filter(doc_name__contains=r)
        dpt=Department.objects.filter( dept_name__contains=r)
        return render(request,'search.html',{'r':r,'doc':doc,'dpt':dpt})
    else:
        return render(request,'search.html',{})


