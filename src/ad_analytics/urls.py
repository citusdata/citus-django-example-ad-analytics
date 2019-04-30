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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic.base import RedirectView


from ad_analytics.views.campaigns import *
from ad_analytics.views.ads import *
from ad_analytics.api.routers import router


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(template_name='ad_analytics/login.html'),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', RedirectView.as_view(url='campaigns'), name='home'),  # same as campaigns
    path('campaigns/', CampaignListView.as_view(), name='campaign_list'),  # uses the LoginRequiredMixin
    path('campaign/<int:pk>/', detail, name='campaign_detail'),  # uses the login_required decorator
    path('campaign/<int:campaign_id>/ad/<int:pk>/', ad_detail, name='campaign_ad_detail'),  # uses the login_required decorator
    path('api/', include((router.urls, 'api'))),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
