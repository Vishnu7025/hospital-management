from django.shortcuts import render
from django import http
from django.http import HttpResponse
from django.shortcuts import render
from. models import Doctors
# Create your views here.
def doctors(request):
      dic_docs = {
            'doctors': Doctors.objects.all()
      }
      return render(request,'doctors.html',dic_docs)

