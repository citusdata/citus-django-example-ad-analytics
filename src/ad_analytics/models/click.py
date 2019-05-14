import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models

from .ads import Ads
from .company import Company


class Click(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE, related_name='clicks')
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                related_name='clicks',
                                null=True)
    site_url = models.TextField()
    cost_per_click_usd = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    user_data = JSONField(null=True, blank=True)
    user_ip = models.CharField(max_length=124)
    clicked_at = models.DateTimeField(null=True)
