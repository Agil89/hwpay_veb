# Generated by Django 5.1.4 on 2025-01-12 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_type', models.CharField(choices=[('cannabis', 'Cannabis'), ('no_cannabis', 'No Cannabis')], max_length=50)),
                ('articles_of_organization', models.FileField(upload_to='uploads/articles/')),
                ('statement_of_information', models.FileField(upload_to='uploads/statements/')),
                ('business_license', models.FileField(upload_to='uploads/licenses/')),
                ('business_address', models.CharField(max_length=255)),
                ('website', models.URLField()),
            ],
        ),
    ]
