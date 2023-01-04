# import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.decorators import login_required
# from django.utils import timezone
from django.shortcuts import get_object_or_404, render
# from django.utils.translation import gettext, gettext_lazy as _
from django.http import HttpResponse
from .forms import DepartmentForm
from .models import Department
# from material.frontend.views import ModelViewSet, ListModelView

from . import models

def index(request):
    # return HttpResponse('<h1>Page was found</h1>')
    form = DepartmentForm()
    dept = Department.objects.all()
    return render(request, "employees/index.html", {'form':form, 'dept':dept})

# @csrf_exempt
def save_data(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            dept_id = request.POST.get('dept_id')
            dept_no = request.POST['dept_no']
            dept_name = request.POST['dept_name']
            if(dept_id ==''):
                dept = Department(dept_no = dept_no, dept_name=dept_name)
            else:
                dept = Department(dept_id=dept_id, dept_no = dept_no, dept_name=dept_name)
            dept.save()
            department = Department.objects.values()
            #print(department)
            department_data = list(department)
            return JsonResponse({'status':'Save', 'department_data':department_data})
        else:
            return JsonResponse({'status':0})
        

# Delete Data
def delete_data(request):
    if request.method == "POST":
        dept_id = request.POST.get('sid')
        #print(dept_id)
        
        dept = Department.objects.get(pk=dept_id)
        dept.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})
    

# Edit Data
def edit_data(request):
    if request.method == "POST":
        dept_id = request.POST.get('sid')
        print(dept_id)
        department = Department.objects.get(pk=dept_id)
        department_data = {"dept_id":department.dept_id, "dept_no":department.dept_no, "dept_name":department.dept_name}
        return JsonResponse(department_data)