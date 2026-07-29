from django.shortcuts import render, HttpResponse
from .models import Customer

# Create your views here.

def index(request):
    customers = Customer.objects.all().order_by("-id")[:15]
    customer_count = Customer.objects.count()

    context={
    	"customers":customers,
    	"customer_count":customer_count
    }
    return render(request, "customer_list.html", context)
	