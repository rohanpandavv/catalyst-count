from django.db import models

class CompanyData(models.Model):
    id = models.CharField(max_length=25, primary_key=True)
    name = models.CharField(max_length=255, null=True)
    domain = models.CharField(max_length=255, null=True)
    year_founded = models.CharField(max_length=11, null=True)
    industry = models.CharField(max_length=50, null=True)
    size_range = models.CharField(max_length=100, null=True)
    locality = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=99, null=True)
    state = models.CharField(max_length=99, null=True)
    country = models.CharField(max_length=99, null=True)
    linkedin_url = models.CharField(max_length=255, null=True)
    cr_emp_est = models.IntegerField(default=0)
    tot_emp_est = models.IntegerField(default=0)