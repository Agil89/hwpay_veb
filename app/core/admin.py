from django.contrib import admin
from .models import BusinessRegistration

@admin.register(BusinessRegistration)
class BusinessRegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'business_type', 'business_address', 'website')
    search_fields = ('business_type', 'business_address', 'website')
    list_filter = ('business_type',)
    ordering = ('-id',)
