from tkinter import CASCADE
from django.db import models
from doctors.models import Doctors
# Create your models here.
class Booking(models.Model):
    g_name = models.CharField(max_length=255)
    p_phone =models.CharField(max_length=10)
    p_email = models.EmailField()
    doc_name =models.ForeignKey(Doctors,on_delete=models.CASCADE )
    booking_date = models.DateField(1)
    booked_on = models.DateField(auto_now=True)