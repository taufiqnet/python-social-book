# import json

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import DepartmentSerializer


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
    return render(request, "employees/index.html")

def department_data(request):
    # return HttpResponse('<h1>Page was found</h1>')
    form = DepartmentForm()
    dept = Department.objects.all()
    return render(request, "employees/department.html", {'form':form, 'dept':dept})

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
    
    
# QuerySet API Methods:

# employee_data = Employee.objects.all()
# employee_data = Employee.objects.filter(salary=10000)
# employee_data = Employee.objects.exclude(salary=10000)
# employee_data = Employee.objects.order_by(salary)
# employee_data = Employee.objects.order_by(-salary)
# employee_data = Employee.objects.order_by(?) #Random Order
# employee_data = Employee.objects.order_by(name) #Asc Order
# employee_data = Employee.objects.order_by(-name) #Desc Order
# employee_data = Employee.objects.order_by(id).reverse()[:5] 

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/department/',
            'method': 'GET',
            'dept_no': None,
            'dept_name': None,
            'description': 'Returns an array of departments'
        },
        {
            'Endpoint': '/department/id',
            'method': 'GET',
            'dept_no': None,
            'dept_name': None,
            'description': 'Returns a single department object'
        },
        {
            'Endpoint': '/department/create/',
            'method': 'POST',
            'dept_no': {'dept_no': ""},
            'dept_name': {'dept_name': ""},
            'description': 'Creates new department with data sent in post request'
        },
        {
            'Endpoint': '/department/id/update/',
            'method': 'PUT',
            'dept_no': {'dept_no': ""},
            'dept_name': {'dept_name': ""},
            'description': 'Creates an existing department with data sent'
        },
        {
            'Endpoint': '/department/id/delete/',
            'method': 'DELETE',
            'dept_no': None,
            'dept_name': None,
            'description': 'Deletes an existing department'
        },
    ]    
    
    #return JsonResponse(routes, safe=False)
    
    return Response(routes)


#fucntion based rest api
@api_view(['GET'])
def getDepartments(request):
    try:
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)
    except Department.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        

@api_view(['GET'])
def getDepartment(request, pk):
    try:
        department = Department.objects.get(dept_id=pk)
        serializer = DepartmentSerializer(department, many=False)
        return Response(serializer.data)
    except Department.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])
def createDepartment(request):
    data = request.data
    
    department = Department.objects.create(
        dept_no=data['dept_no'],
        dept_name=data['dept_name']
    )
    serializer = DepartmentSerializer(department, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def updateDepartment(request, pk):    
    department = Department.objects.get(dept_id=pk)
    serializer = DepartmentSerializer(department, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteDepartment(request, pk):
    department = Department.objects.get(dept_id=pk)
    department.delete()
    return Response('Department was deleted!')


#class based rest API
