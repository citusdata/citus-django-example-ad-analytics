from django.db import models

from django_multitenant.mixins import *

from .base import TenantManager


def get_image_path(instance, filename):
    return os.path.join('images', 'companies', get_filename(filename))


class Company(TenantModelMixin, models.Model):
    name = models.TextField()
    image = models.ImageField(upload_to=get_image_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
    ceo = models.OneToOneField('ad_analytics.Employee', null=True,
                               on_delete=models.SET_NULL,
                               related_name='ceo_companies')

    tenant_id = 'id'
    objects = TenantManager()
