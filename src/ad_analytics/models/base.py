from django_multitenant.mixins import *

class TenantManager(TenantManagerMixin, models.Manager):
    pass
