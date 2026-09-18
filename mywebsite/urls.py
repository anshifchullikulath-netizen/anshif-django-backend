from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.enquiry, name='enquiry'),
    path('success/', views.success, name='success'),
]