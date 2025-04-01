from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import BusinessRegistration

@receiver(post_save, sender=BusinessRegistration)
def send_registration_email(sender, instance, created, **kwargs):
    if created:
        subject = "New Business Registration Submitted"
        message = f"""
        A new business registration has been submitted.

        Company Name: {instance.company_name}
        Business Type: {instance.business_type}
        Contact Name: {instance.name}
        Email: {instance.email}
        Phone Number: {instance.phone_number}

        Address: {instance.business_address}
        Website: {instance.website}
        """

        recipient_list = ['k22n.auto@gmail.com']
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
