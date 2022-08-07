from django import forms
from. models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        labels = {
           'g_name':'Patient Name',
           'p_phone':'Phone Number',
           'p_email':'Email',
           'dep_name':'Department Name',
           'doc_name':'Doctor Name',
           'booking_date':'Booking Date',
        }
       

        widgets = {
            'booking_date': DateInput(),
            
        }
      