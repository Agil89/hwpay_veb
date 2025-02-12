from django.db import models

class BusinessRegistration(models.Model):
    BUSINESS_TYPE_CHOICES = [
        ('cannabis', 'Cannabis'),
        ('no_cannabis', 'No Cannabis'),
    ]

    business_type = models.CharField(max_length=50, choices=BUSINESS_TYPE_CHOICES)
    articles_of_organization = models.FileField(upload_to='uploads/articles/', blank=True, null=True)
    statement_of_information = models.FileField(upload_to='uploads/statements/', blank=True, null=True)
    business_license = models.FileField(upload_to='uploads/licenses/', blank=True, null=True)
    business_address = models.CharField(max_length=255)
    website = models.URLField()
    company_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.company_name} - {self.business_address}"