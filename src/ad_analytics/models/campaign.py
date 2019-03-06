from django.contrib.postgres.fields import ArrayField
from django.db import models

from .company import Company


class Campaign(models.Model):
    company = models.ForeignKey(Company, related_name='campaigns', on_delete=models.CASCADE)
    name = models.TextField()
    monthly_budget = models.IntegerField(null=True)
    blacklisted_site_urls = ArrayField(models.CharField(max_length=200), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
