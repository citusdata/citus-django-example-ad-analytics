from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.views.generic import ListView, DetailView

from ad_analytics.models import Campaign, Ads


class CampaignListView(LoginRequiredMixin, ListView):
    model = Campaign
    template_name = 'ad_analytics/campaigns/list.html'
    context_object_name = 'campaigns'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(company=self.request.user.employee.company)\
                       .prefetch_related('ads')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = self.request.user.employee.company

        for campaign in context['campaigns']:
            if self.request.user in campaign.collaborators.all():
                campaign.is_collaborator = True

        return context



class CampaignDetailView(DetailView):
    model = Campaign
    template_name = 'ad_analytics/campaigns/detail.html'
    context_object_name = 'campaign'

    def get_context_data(self, **kwargs):
        context = super(CampaignDetailView, self).get_context_data(**kwargs)
        company = self.request.user.employee.company
        context['company'] = company
        context['campaigns'] = company.campaigns.all().prefetch_related('ads')

        campaign = self.get_object()
        context['ads'] = campaign.ads.all()

        return context


detail = login_required(CampaignDetailView.as_view())
