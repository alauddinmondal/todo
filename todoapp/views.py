from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import EmpregisterForm
from .models import *

# Create your views here.


def employee_list(request):
    emplist = Employee.objects.all()
    context = {'emplist':emplist}
    template = 'emp_register/emplist.html'
    return render(request, template, context)


def employee_form(request,id=0):
    if request.method=='GET':
        if id == 0:
            form = EmpregisterForm() #this is normal form
        else:
            getemplist = Employee.objects.get(pk=id)
            form = EmpregisterForm(instance=getemplist) #this is for form RETRIEVE
        template = 'emp_register/empform.html'
    else:
        if id == 0:
            form = EmpregisterForm(request.POST) #This is for normal post
        else:
            emplist_update = Employee.objects.get(pk=id)
            form = EmpregisterForm(request.POST, instance=emplist_update) #This is for form RETRIEVE AND POST

        if form.is_valid():
            form.save()
        return redirect('/employee/list')

    return render(request, template, {'form': form})


def employee_delete(request, id):
    emp = Employee.objects.get(pk=id)
    emp.delete()
    return redirect('/employee/list')

