from django.contrib import admin
from .models import Customer, Job, Team_Member

# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'extracted_id']
    search_fields = ['first_name', 'last_name', 'full_name', 'email', 'extracted_id']
    list_display_links = ['full_name']

@admin.register(Job) 
class JobAdmin(admin.ModelAdmin):
    search_fields = ['title', "main_dispatch"]

admin.site.register(Team_Member)