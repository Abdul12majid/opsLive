from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Customer, Job, Customer_Comment
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def list_customers(request):
    customers = Customer.objects.all().order_by("-id")[:15]
    customer_count = Customer.objects.count()

    context={
    	"customers":customers,
    	"customer_count":customer_count
    }
    return render(request, "customer/customer_list.html", context)

def list_jobs(request):
    jobs = Job.objects.all().order_by("-id")[:15]
    job_count = Job.objects.count()

    context={
        "jobs":jobs,
        "job_count":job_count
    }
    return render(request, "job/job_list.html", context)

def customer_details(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    context={
    	"customer": customer,
        "jobs": customer.jobs.all().order_by("-id"),
    }
    return render(request, "customer/customer_details.html", context)

def job_details(request, pk):
    job = get_object_or_404(Job, pk=pk)

    context={
    	"job": job,
    }
    return render(request, "job/job_info.html", context)

def get_comment_user_info(user):
    if not user:
        return {
            "name": "Unknown User",
            "initials": "UU",
        }

    name = user.get_full_name().strip()

    if not name:
        name = user.username

    name_parts = name.split()

    if len(name_parts) >= 2:
        initials = (
            name_parts[0][0] +
            name_parts[1][0]
        ).upper()
    else:
        initials = name[:2].upper()

    return {
        "name": name,
        "initials": initials,
    }

@login_required(login_url='login_user_mobile')
def customer_comments(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    comments = customer.customer_comments.select_related(
        'created_by'
    ).order_by('-uploaded_at')

    data = []

    for comment in comments:

        user_info = get_comment_user_info(
            comment.created_by
        )

        data.append({
            'id': comment.id,
            'comment': comment.the_comment,
            'created_by': user_info['name'],
            'initials': user_info['initials'],
            'uploaded_at': comment.uploaded_at.strftime(
                '%b %d, %Y %I:%M %p'
            ),
        })

    return JsonResponse({
        'success': True,
        'comments': data,
    })

@login_required(login_url='login_user_mobile')
@require_http_methods(["POST"])
def add_customer_comment(request, pk):

    customer = get_object_or_404(
        Customer,
        pk=pk
    )

    comment_text = request.POST.get(
        'the_comment',
        ''
    ).strip()

    if not comment_text:
        return JsonResponse({
            'success': False,
            'message': 'Comment cannot be empty.'
        }, status=400)

    comment = Customer_Comment.objects.create(
        owner=customer,
        created_by=request.user,
        the_comment=comment_text,
    )

    user_info = get_comment_user_info(
        request.user
    )

    return JsonResponse({
        'success': True,
        'message': 'Note saved',

        'comment': {
            'id': comment.id,
            'comment': comment.the_comment,
            'created_by': user_info['name'],
            'initials': user_info['initials'],
            'uploaded_at': comment.uploaded_at.strftime(
                '%b %d, %Y %I:%M %p'
            ),
        }
    })

@login_required(login_url='login_user_mobile')
@require_http_methods(["POST"])
def delete_customer_comment(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    comment_id = request.POST.get('comment_id')

    comment = get_object_or_404(
        Customer_Comment,
        id=comment_id,
        owner=customer
    )

    comment.delete()

    return JsonResponse({
        'success': True,
        'message': 'Note deleted'
    })