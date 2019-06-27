import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models
from django_multitenant.mixins import *
from django_multitenant.fields import TenantForeignKey

from .ads import Ads
from .company import Company

class TenantManager(TenantManagerMixin, models.Manager):
    pass


class Impression(TenantModelMixin, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ads = TenantForeignKey(Ads, on_delete=models.CASCADE, related_name='impressions')
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                related_name='impressions',
                                null=True)

    site_url = models.TextField()
    cost_per_impression_usd = models.DecimalField(max_digits=20, decimal_places=10,
                                                  null=True)
    user_data = JSONField(null=True, blank=True)
    user_ip = models.CharField(max_length=124)
    seen_at = models.DateTimeField()

    tenant_id = 'company_id'
    objects = TenantManager()
