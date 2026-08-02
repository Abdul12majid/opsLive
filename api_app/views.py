from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from .serializers import CustomerSerializer, JobSerializer
from ops_app.models import Customer, Job, Team_Member
from rest_framework import status
from django.utils import timezone
from rest_framework.response import Response

# Create your views here.
def index(request):
	return HttpResponse("API APP")

@api_view(['GET', 'POST'])
def customer_list_create(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        extracted_id = request.data.get("extracted_id")
        email = request.data.get("email")
        first_phone = request.data.get("first_phone")
        address = (request.data.get("address") or "").strip().upper()

        existing_customer = None

        # 1. Check extracted_id first
        if extracted_id:
            existing_customer = Customer.objects.filter(
                extracted_id=extracted_id
            ).first()

        # 2. Check phone + address match
        if not existing_customer and first_phone:
            customers = Customer.objects.filter(
                first_phone=first_phone
            )

            for customer in customers:
                customer_address = (customer.address or "").strip().upper()

                if customer_address == address:
                    existing_customer = customer
                    break

        # 3. Fallback email match
        if not existing_customer and email:
            existing_customer = Customer.objects.filter(
                email__iexact=email
            ).first()

        # Existing customer found
        if existing_customer:
            serializer = CustomerSerializer(existing_customer)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Create new customer
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_job(request):
    title = request.data.get("title")
    link_id = request.data.get("link_id")
    recall_link_id = request.data.get("recall_link_id")     # phone
    recall_link_id2 = request.data.get("recall_link_id2")   # email
    description = request.data.get("description")

    if not title:
        return Response(
            {"error": "title is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        customer = None

        # GLOBAL PHONE / EMAIL CHECK FIRST
        if recall_link_id or recall_link_id2:

            if recall_link_id:
                customers = Customer.objects.filter(first_phone=recall_link_id)
                t_customer = customers.first()
                if t_customer and t_customer.id == 1161:
                    customer = customers.last()
                else:
                    customer = t_customer

            if not customer and recall_link_id2:
                customers = Customer.objects.filter(email__iexact=recall_link_id2)
                t_customer = customers.first()
                if t_customer and t_customer.id == 1161:
                    customer = customers.last()
                else:
                    customer = t_customer

            # PREFIX ONLY IF CUSTOMER HAD JOB BEFORE TODAY
            if customer:
                today_start = timezone.now().replace(
                    hour=0, minute=0, second=0, microsecond=0
                )

                had_previous_job = Job.objects.filter(
                    customer=customer,
                    created_at__lt=today_start
                ).exists()

                if had_previous_job and not title.startswith("EXISTING CS"):
                    title = f"EXISTING CS {title}"

        # IF CUSTOMER NOT FOUND → CONTINUE NORMAL FLOW
        if not customer:

            if "RECALL" in title.upper():

                if not recall_link_id and not recall_link_id2:
                    return Response(
                        {"error": "recall_link_id or recall_link_id2 is required for RECALL jobs"},
                        status=status.HTTP_400_BAD_REQUEST
                    )

                if recall_link_id:
                    customers = Customer.objects.filter(first_phone=recall_link_id)
                    t_customer = customers.first()
                    if t_customer and t_customer.id == 1161:
                        customer = customers.last()
                    else:
                        customer = t_customer

                if not customer and recall_link_id2:
                    customers = Customer.objects.filter(email__iexact=recall_link_id2)
                    t_customer = customers.first()
                    if t_customer and t_customer.id == 1161:
                        customer = customers.last()
                    else:
                        customer = t_customer

                if not customer:
                    # fallback to normal creation flow instead of failing
                    if not link_id:
                        return Response(
                            {"error": "link_id is required to create new customer"},
                            status=status.HTTP_400_BAD_REQUEST
                        )

                    customer = Customer.objects.get(extracted_id=link_id)

            else:
                if not link_id:
                    return Response(
                        {"error": "link_id is required"},
                        status=status.HTTP_400_BAD_REQUEST
                    )

                customer = Customer.objects.get(extracted_id=link_id)

    except Customer.DoesNotExist:
        return Response(
            {"error": "Customer not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    # ---- ASSIGNED WORKER ----
    try:
        assigned_worker = Team_Member.objects.get(user_id="123456")
    except Team_Member.DoesNotExist:
        return Response(
            {"error": "Team member 123456 does not exist"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    # ---- SERIALIZER ----
    data = request.data.copy()
    data["title"] = title

    serializer = JobSerializer(data=data)

    if serializer.is_valid():

        extra_fields = {
            "customer": customer,
            "assigned_to": assigned_worker
        }

        job = serializer.save(**extra_fields)

        return Response(
            JobSerializer(job).data,
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)