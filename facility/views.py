from django.shortcuts import render
from django import http
from django.http import HttpResponse
from django.shortcuts import render
from. models import Departments
# Create your views here.
def departments(request):
      dic_dept = {
            'dept' : Departments.objects.all()
      }
      return render(request,'facility.html',dic_dept)
