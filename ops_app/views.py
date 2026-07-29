from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Customer, Job

# Create your views here.

def list_customers(request):
    customers = Customer.objects.all().order_by("-id")[:15]
    customer_count = Customer.objects.count()

    context={
    	"customers":customers,
    	"customer_count":customer_count
    }
    return render(request, "customer/customer_list.html", context)


def customer_details(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    context={
    	"customer": customer,
        "jobs": customer.jobs.all().order_by("-id"),
	    "map_min_lon": customer.longitude - 0.01,
	    "map_min_lat": customer.latitude - 0.01,
	    "map_max_lon": customer.longitude + 0.01,
	    "map_max_lat": customer.latitude + 0.01,
    }
    return render(request, "customer/customer_details.html", context)


def job_details(request, pk):
    job = get_object_or_404(Job, pk=pk)

    context={
    	"job": job,
    }
    return render(request, "job/job_info.html", context)
	