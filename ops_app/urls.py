from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_customers),
    path('customer/<int:pk>/', views.customer_details, name="customer_details")
]