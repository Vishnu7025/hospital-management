from django.shortcuts import render
from django.http import HttpResponse
from.forms import BookingForm
from django.contrib import messages
# Create your views here.
def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"We have recived your appointment request,Our representative will call you")
    form = BookingForm()
    dic_form = {
        'form': form
    }
    return render(request,'booking.html',dic_form)

