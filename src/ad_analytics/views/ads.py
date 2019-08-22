from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from django_multitenant.utils import get_current_tenant

from ad_analytics.models import Ads


class AdDetailView(DetailView):
    model = Ads
    template_name = 'ad_analytics/ads/detail.html'


    def get_context_data(self, **kwargs):
        context = super(AdDetailView, self).get_context_data(**kwargs)
        company = get_current_tenant()
        context['company'] = company
        context['campaigns'] = company.campaigns.all().prefetch_related('ads')

        return context


ad_detail = login_required(AdDetailView.as_view())
