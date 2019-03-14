"""ad_analytics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from ad_analytics.views.authenticate import *
from ad_analytics.views.campaigns import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path(r'login/', login),
    path(r'logout/', logout, name='logout'),

    path('campaigns/', CampaignListView.as_view(), name='campaign_list'),  # uses the LoginRequiredMixin
    path('campaign/<int:pk>/', detail, name='campaign_detail'),  # uses the login_required decorator

]
