from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_customers, name='customers'),
    path('customer/<int:pk>/', views.customer_details, name="customer_details"),
    path('job/<int:pk>/', views.job_details, name="job_details")
]