import imp
from tabnanny import verbose
from django.db import models

from facility import views
from facility.models import Departments

# Create your models here.port Departments

class Doctors(models.Model):
    doc_name = models.CharField(max_length=255)
    doc_spec = models.CharField(max_length=255)
    dep_name = models.ForeignKey(Departments,on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors')

    class Meta:
        verbose_name= 'Doctors'
        verbose_name_plural  = 'Doctors'

    def __str__(self):
        return 'Dr ' +  self.doc_name + ' - (' + self.doc_spec + ')'
