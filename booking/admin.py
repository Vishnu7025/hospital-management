from django.contrib import admin
from.models import Booking
# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','g_name','p_phone','p_email','doc_name','booking_date','booked_on')
admin.site.register(Booking,BookingAdmin)