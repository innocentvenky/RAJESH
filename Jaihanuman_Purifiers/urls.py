from django.contrib import admin
from django.urls import path
from Jaihanuman_Purifiers import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Home),
    path("service/",views.service),
    path("feedback/",views.feedback),
    path("booking/",views.booking),
    path('details/',views.data)
]
