from django import forms
from . models import Serivce,FeedBack
class ServiceForm(forms.ModelForm):
    class Meta:
        model=Serivce
        fields='Name','Phone','Address','Problem','Model'
class FeedbackForm(forms.ModelForm):
    class Meta:
        model=FeedBack
        fields='__all__'
