from django.contrib import admin
from .models import JobListing, Company, Individual, VerifiedJobListing

admin.site.register(JobListing)
admin.site.register(Company)
admin.site.register(Individual)
admin.site.register(VerifiedJobListing)

