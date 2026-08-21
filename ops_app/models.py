from django.db import models
import re
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    customer_id = models.CharField(max_length=50, blank=True, null=True)
    extracted_id = models.CharField(max_length=50, blank=True, null=True)
    invoice_id = models.CharField(max_length=50, blank=True, null=True)
    tech_id = models.CharField(max_length=50, blank=True, null=True)
    auth_url = models.TextField(blank=True, null=True)
    second_auth_url = models.TextField(blank=True, null=True)

    first_phone = models.CharField(max_length=50, blank=True, null=True)
    the_second_phone = models.CharField(max_length=50, blank=True, null=True)
    secondary_contact = models.CharField(max_length=300, blank=True, null=True)
    message_to_number = models.CharField(max_length=300, blank=True, null=True)
    invoice_id = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    
    address = models.CharField(max_length=300, blank=True, null=True)
    unit = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=50, blank=True, null=True)
    location_id = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    job_id = models.CharField(max_length=50, blank=True, null=True)

    order_id_1 = models.CharField(max_length=255, blank=True, null=True)
    order_id_2 = models.CharField(max_length=255, blank=True, null=True)
    order_id_3 = models.CharField(max_length=255, blank=True, null=True)

    tracking_id_1 = models.CharField(max_length=255, blank=True, null=True)
    track_1_scanned = models.BooleanField(default=False)
    one_last_scanned = models.BooleanField(default=False)

    tracking_id_2 = models.CharField(max_length=255, blank=True, null=True)
    track_2_scanned = models.BooleanField(default=False)
    two_last_scanned = models.BooleanField(default=False)

    tracking_id_3 = models.CharField(max_length=255, blank=True, null=True)
    track_3_scanned = models.BooleanField(default=False)
    three_last_scanned = models.BooleanField(default=False)

    total_item = models.TextField(blank=True, null=True)
    customer_notes = models.TextField(blank=True, null=True)
    scanned = models.BooleanField(default=False)
    scanned_date = models.DateTimeField(auto_now_add=True)

    provider = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def full_address(self):
        raw = f"{self.address}, {self.city}, {self.state} {self.zip_code}, UK"
        return re.sub(r"\s+", " ", raw).strip()

    @property
    def formatted_phone(self):
        if not self.first_phone:
            return ""
        x_str = str(self.first_phone)
        if len(x_str) == 10:
            return f"({x_str[:3]}) {x_str[3:6]}-{x_str[6:]}"
        return self.first_phone

    @property
    def formatted_phone2(self):
        if not self.the_second_phone:
            return ""
        x_str = str(self.the_second_phone)
        if len(x_str) == 10:
            return f"({x_str[:3]}) {x_str[3:6]}-{x_str[6:]}"
        return self.the_second_phone

    def __str__(self):
        return self.full_name 

class Customer_Comment(models.Model):
    owner = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='customer_comments'
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    the_comment = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(default=timezone.now)

class Team_Member(models.Model):
    full_name = models.CharField(max_length=300, blank=True, null=True)
    user_id = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.full_name

def job_attachment_report_path(instance, filename):

    job = instance
    customer = job.customer

    # --- Safe customer name & appliance ---
    customer_name = clean_name(customer.full_name, 30)
    appliance = clean_name(job.appliance or "appliance", 20)

    # --- Timestamp: DDMMYYHHMMSS ---
    timestamp = datetime.now().strftime("%d%m%y%H%M%S")

    # --- Customer folder ---
    customer_folder = f"customer_attachments/{customer_name}_{customer.extracted_id}"

    # --- Report folder ---
    report_folder = f"{customer_folder}/jobs/report"

    # Ensure directory exists
    full_path = os.path.join(settings.MEDIA_ROOT, report_folder)
    os.makedirs(full_path, exist_ok=True)

    # --- Final filename ---
    filename = f"{timestamp}_{customer_name}_{appliance}.pdf"

    return f"{report_folder}/{filename}"
    
class Job(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('Pending', 'Pending'),
        ('Scheduled', 'Scheduled'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    title = models.CharField(max_length=300, blank=True, null=True)
    appliance = models.CharField(max_length=300, blank=True, null=True)
    brand = models.CharField(max_length=300, blank=True, null=True)
    model = models.CharField(max_length=300, blank=True, null=True)
    link_id = models.CharField(max_length=300, blank=True, null=True)
    recall_link_id = models.CharField(max_length=300, blank=True, null=True)
    main_dispatch = models.CharField(max_length=300, blank=True, null=True)
    recall_link_id2 = models.CharField(max_length=300, blank=True, null=True)
    sub_title = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    job_history = models.TextField(blank=True, null=True)
    job_id = models.CharField(max_length=50, blank=True, null=True)
    smartautho = models.BooleanField(blank=True, null=True, default=False)
    rating = models.IntegerField(
        choices=[
            (None, 'None'),
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
        ],
        null=True,
        blank=True,
        default=None,
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='jobs'
    )
    assigned_to = models.ForeignKey(
        Team_Member,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_jobs'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='New'
    )
    order_id_1 = models.CharField(max_length=255, blank=True, null=True)
    order_id_2 = models.CharField(max_length=255, blank=True, null=True)
    order_id_3 = models.CharField(max_length=255, blank=True, null=True)
    order_id_4 = models.CharField(max_length=255, blank=True, null=True)
    order_id_5 = models.CharField(max_length=255, blank=True, null=True)

    tracking_id_1 = models.CharField(max_length=255, blank=True, null=True)
    track_1_scanned = models.BooleanField(default=False)
    one_last_scanned = models.BooleanField(default=False)
    one_scanned_date = models.DateTimeField(null=True, blank=True)

    tracking_id_2 = models.CharField(max_length=255, blank=True, null=True)
    track_2_scanned = models.BooleanField(default=False)
    two_last_scanned = models.BooleanField(default=False)
    two_scanned_date = models.DateTimeField(null=True, blank=True)

    tracking_id_3 = models.CharField(max_length=255, blank=True, null=True)
    track_3_scanned = models.BooleanField(default=False)
    three_last_scanned = models.BooleanField(default=False)
    three_scanned_date = models.DateTimeField(null=True, blank=True)

    tracking_id_4 = models.CharField(max_length=255, blank=True, null=True)
    track_4_scanned = models.BooleanField(default=False)
    four_last_scanned = models.BooleanField(default=False)
    four_scanned_date = models.DateTimeField(null=True, blank=True)

    tracking_id_5 = models.CharField(max_length=255, blank=True, null=True)
    track_5_scanned = models.BooleanField(default=False)
    five_last_scanned = models.BooleanField(default=False)
    five_scanned_date = models.DateTimeField(null=True, blank=True)

    scanned_date = models.DateTimeField(null=True, blank=True)

    cost_1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cost_2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cost_3 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cost_4 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cost_5 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    date_1 = models.DateTimeField(blank=True, null=True)
    date_2 = models.DateTimeField(blank=True, null=True)
    date_3 = models.DateTimeField(blank=True, null=True)
    date_4 = models.DateTimeField(blank=True, null=True)
    date_5 = models.DateTimeField(blank=True, null=True)

    job_note = models.TextField(blank=True, null=True)
    problem = models.TextField(blank=True, null=True)
    field_note = models.TextField(blank=True, null=True)
    diag_note = models.TextField(blank=True, null=True)
    done_diag = models.BooleanField(blank=True, null=True, default=False)
    level_note = models.TextField(blank=True, null=True, default=" ")
    sub_text = models.TextField(blank=True, null=True)

    parts_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    labor_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_voice_autho = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_smart_autho = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ltd_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    current_step_due_date = models.DateTimeField(blank=True, null=True)
    current_task_due_date = models.DateTimeField(blank=True, null=True)
    scheduled_date = models.DateTimeField(blank=True, null=True)
    event_id = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_scheduled = models.BooleanField(blank=True, null=True, default=False)
    is_completed = models.BooleanField(blank=True, null=True, default=False)
    is_cancelled = models.BooleanField(blank=True, null=True, default=False)
    admin_mode = models.BooleanField(blank=True, null=True, default=False)
    autho_mode = models.BooleanField(blank=True, null=True, default=False)
    survey_follow_up_mode = models.BooleanField(blank=True, null=True, default=False)

    needs_authorization = models.BooleanField(default=False, null=True, blank=True)
    date_authorized = models.DateTimeField(blank=True, null=True)
    needs_invoice = models.BooleanField(default=False, null=True, blank=True)
    repair_job = models.BooleanField(default=False, null=True, blank=True)
    invoice_paid = models.BooleanField(default=False, null=True, blank=True)
    management_approved = models.BooleanField(default=False, null=True, blank=True)

    autho_due_date = models.DateTimeField(blank=True, null=True)
    autho_type = models.CharField(max_length=255, blank=True, null=True)
    report_pdf = models.FileField(
        upload_to=job_attachment_report_path,
        null=True,
        blank=True
    )


    @property
    def total_cost(self):
        return sum(filter(None, [
            self.cost_1 or Decimal("0"),
            self.cost_2 or Decimal("0"),
            self.cost_3 or Decimal("0"),
            self.cost_4 or Decimal("0"),
            self.cost_5 or Decimal("0"),
        ]))

    def __str__(self):
        return f"{self.title} - {self.customer.full_name}"