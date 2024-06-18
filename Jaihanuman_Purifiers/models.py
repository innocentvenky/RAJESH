from django.db import models
from django.utils import timezone

# Create your models here.
class Serivce(models.Model):
    Name=models.CharField(max_length=40)
    Phone=models.PositiveIntegerField()
    Address=models.CharField(max_length=100)
    Problem=models.CharField(max_length=100)
    Model=models.CharField(max_length=40)
    about=models.CharField(max_length=100,default='NULL')
class FeedBack(models.Model):
    Name=models.CharField(max_length=30)
    feedback=models.TextField()
class Booking(models.Model):
    Name=models.CharField(max_length=50)
    Phone=models.PositiveBigIntegerField()
    Email=models.EmailField()
    Address=models.CharField(max_length=100)
    Booking_date=models.DateField(default=timezone.now)
    Delivery_date=models.DateField(default='0000-00-00')
    Install_details=models.CharField(max_length=100,default='null')

