from django.db import models

from django_multitenant.mixins import *
from django_multitenant.fields import TenantForeignKey


def get_image_path(instance, filename):
    return os.path.join('images', 'companies', get_filename(filename))


class TenantManager(TenantManagerMixin, models.Manager):
    pass

class Company(TenantModelMixin, models.Model):
    name = models.TextField()
    image = models.ImageField(upload_to=get_image_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
    ceo = TenantForeignKey('ad_analytics.Employee', null=True,
                           on_delete=models.SET_NULL,
                           related_name='ceo_companies')

    tenant_id = 'id'
    objects = TenantManager()
