import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models

from .ads import Ads


class Impression(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE, related_name='impressions')
    site_url = models.TextField()
    cost_per_impression_usd = models.DecimalField(max_digits=20, decimal_places=10,
                                                  null=True)
    user_data = JSONField(null=True, blank=True)
    user_ip = models.CharField(max_length=124)
    seen_at = models.DateTimeField()
