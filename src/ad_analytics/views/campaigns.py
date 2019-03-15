from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from ad_analytics.models import Campaign


class CampaignListView(LoginRequiredMixin, ListView):
    model = Campaign
    template_name = 'ad_analytics/campaigns/list.html'
    context_object_name = 'campaigns'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(company=self.request.user.employee.company)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = self.request.user.employee.company
        return context



class CampaignDetailView(DetailView):
    model = Campaign
    template_name = 'ad_analytics/campaigns/detail.html'
    context_object_name = 'campaign'

    def get_context_data(self, **kwargs):
        context = super(CampaignListView, self).get_context_data(**kwargs)
        context['company'] = request.user.employee.company

        return context


detail = login_required(CampaignDetailView.as_view())
