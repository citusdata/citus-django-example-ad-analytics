from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from ad_analytics.models import Campaign


class CampaignListView(LoginRequiredMixin, ListView):
    model = Campaign
    template_name = 'ad_analytics/campaigns/list.html'



class CampaignDetailView(DetailView):
    model = Campaign
    template_name = 'ad_analytics/campaigns/detail.html'

detail = login_required(CampaignDetailView.as_view())
