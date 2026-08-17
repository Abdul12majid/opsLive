from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_customers, name='customers'),
    path('customer/<int:pk>/', views.customer_details, name="customer_details"),
    path('job/<int:pk>/', views.job_details, name="job_details"),
    path('customer/<int:pk>/comments/', views.customer_comments, name='customer_comments'),
    path('customer/<int:pk>/comments/add/', views.add_customer_comment, name='add_customer_comment'),
    path('customer/<int:pk>/comments/delete/', views.delete_customer_comment, name='delete_customer_comment'),
]