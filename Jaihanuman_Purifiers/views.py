from django.shortcuts import render,redirect
from . models import FeedBack,Booking
from . forms import ServiceForm,FeedbackForm
# Create your views here.
def Home(request):
    return render(request,'Home.html')
def service(request):
    form=ServiceForm()
    if request.method=='POST':
        form=ServiceForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request,"thanks.html")
    return render(request,'service.html',{'form':form})
def feedback(request):
    form=FeedbackForm()
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("/feedback")
    data=FeedBack.objects.all()
    return render(request,'feedback.html',{'form':form,'data':data}) 
def booking(request):
    return render(request,'booking.html')
def data(request):
    detail=Booking.objects.get(id=id)
    return render(request,'details.html',{'detail':detail})


   