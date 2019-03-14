from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.functional import cached_property

from .company import Company
from .employee import Employee


class Campaign(models.Model):
    NEW = 0
    RUNNING = 1
    PAUSED = 2
    ARCHIVED = 3
    STATE_CHOICES = (
        (NEW, 'New'),
        (RUNNING, 'Running'),
        (PAUSED, 'Paused'),
        (ARCHIVED, 'Archived'),
    )
    company = models.ForeignKey(Company, related_name='campaigns', on_delete=models.CASCADE)
    name = models.TextField()
    state = models.IntegerField(choices=STATE_CHOICES,
                                default=NEW)
    monthly_budget = models.IntegerField(null=True)
    blacklisted_site_urls = ArrayField(models.CharField(max_length=200), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
    collaborators = models.ManyToManyField(Employee)


    @cached_property
    def ctr(self):
        return 0
