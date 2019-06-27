from django.contrib.auth.models import User
from django.db import models
from django_multitenant.mixins import *

from .company import Company


class TenantManager(TenantManagerMixin, models.Manager):
    pass


class Employee(TenantModelMixin, models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    tenant_id = 'company_id'
    objects = TenantManager()

    class Meta:
        unique_together=(('company', 'user'))
