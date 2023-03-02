from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
from .models import Employee,Department,Role
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html')
def all_emp(request):
    empall = Employee.objects.all()
    context={
        'empall' : empall 
    }
    print("context",context)
    return render(request,'emp_info.html',context)

def add_emp(request):
    if request.method == 'POST':
        print("post")
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = int(request.POST['dept'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = int(request.POST['role'])
        phone_number = int(request.POST['phone_number'])
        # hire_date = request.POST['hire_date']
        save_emp = Employee(first_name=first_name,last_name=last_name,dept_id=dept,salary=salary,bonus=bonus,role_id=role,phone_number=phone_number,hire_date=datetime.now())
        save_emp.save()
        return HttpResponse("Employee added successfully")
    elif request.method == 'GET':
        print("get")
        return render(request,'add.html')
    else:
        return HttpResponse("Employee details failed to add")

def remove_emp(request,empall_id = 0):
    if empall_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=empall_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee deleted successfully")
        except:
            return HttpResponse("Exception occured")
    empall = Employee.objects.all()
    context={
        'empall' : empall 
    }
    print("context",context)
    return render(request,'remove.html',context)

def filter_emp(request):
    if request.method == 'POST':
        name=request.POST['name']
        # dept=request.POST['dept']
        # role=request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(first_name="siva")
        # if dept:
        #     emps=emps.filter(dept__name = dept)
        # if role:
        #     emps=emps.filter(role__name=role)
        context = {
            'emps' :emps
        }
        print("context111",context)
        return render(request,'emp_info.html',context)
    elif request.method == 'GET':
        return render(request,'filter.html')
    else:
        return HttpResponse("failed to filter")

