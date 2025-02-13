import os
from django.conf import settings
from django.shortcuts import render, redirect
from .models import BusinessRegistration
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def contact_form(request):
    if request.method == 'POST':
        business_type = request.POST.get('business_type')
        business_address = request.POST.get('business_address')
        website = request.POST.get('website')
        company_name = request.POST.get('company_name')
        name = request.POST.get('name')
        job_title = request.POST.get('job_title')
        phone_number = request.POST.get('phone')
        email = request.POST.get('email')

        # Handle file uploads
        articles_of_organization = request.FILES.get('articles_of_organization')
        statement_of_information = request.FILES.get('statement_of_information')
        business_license = request.FILES.get('business_license')

        # Save files to the media directory
        articles_path = save_file(articles_of_organization, 'articles') if articles_of_organization else None
        statement_path = save_file(statement_of_information, 'statements') if statement_of_information else None
        license_path = save_file(business_license, 'licenses') if business_license else None

        # Save data to the database
        registration = BusinessRegistration.objects.create(
            business_type=business_type,
            business_address=business_address,
            website=website,
            company_name=company_name,
            name=name,
            job_title=job_title,
            phone_number=phone_number,
            email=email,
            articles_of_organization=articles_path,
            statement_of_information=statement_path,
            business_license=license_path
        )

        # Add a success message
        messages.success(request, 'Success')

        # Redirect to the index page
        return redirect('index')

    return render(request, 'contact_form.html')

def save_file(file, folder):
    folder_path = os.path.join(settings.MEDIA_ROOT, folder)
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, file.name)
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return f"{folder}/{file.name}"
