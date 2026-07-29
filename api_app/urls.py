from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('customers/', views.customer_list_create, name='customer-list-create'),
    path('jobs/create/', views.create_job, name='create-job'),
]