from django.contrib import admin
from . models import Serivce,FeedBack,Booking
# Register your models here.
class Seriveadmin(admin.ModelAdmin):
    list_display=['Name','Phone','Address','Problem','model','about']
admin.site.register(Serivce,Seriveadmin)
class FeedbackAmin(admin.ModelAdmin):
    list_display=['feedback','Name']
admin.site.register(FeedBack,FeedbackAmin)
class BookingAdmin(admin.ModelAdmin):
    list_display=['Name','Phone','Email','Address','Booking_date','Delivery_date','Install_details']
admin.site.register(Booking,BookingAdmin)
