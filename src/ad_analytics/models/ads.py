from django.contrib.postgres.fields import ArrayField
from django.db import models

from django_multitenant.mixins import *
from django_multitenant.fields import TenantForeignKey

from .campaign import Campaign
from .company import Company


class TenantManager(TenantManagerMixin, models.Manager):
    pass


def get_image_path(instance, filename):
    return os.path.join('images', 'ads', get_filename(filename))


class Ads(TenantModelMixin, models.Model):
    name = models.TextField()
    campaign = TenantForeignKey(Campaign, on_delete=models.CASCADE,
                                 related_name='ads')
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                related_name='ads',
                                null=True)
    image = models.ImageField(upload_to=get_image_path)
    target_url = models.TextField()
    impressions_count = models.BigIntegerField(default=0)
    clicks_count = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    tenant_id = 'company_id'
    objects = TenantManager()
