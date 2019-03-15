from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from ad_analytics.models import Ads


class AdDetailView(DetailView):
    model = Ads
    template_name = 'ad_analytics/ads/detail.html'

ad_detail = login_required(AdDetailView.as_view())
