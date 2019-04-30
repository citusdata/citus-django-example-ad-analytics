from rest_framework import viewsets
from rest_framework import permissions

from .serializers import *


class ClickViewSet(viewsets.ModelViewSet):
    serializer_class = ClickSerializer
    queryset = Click.objects.all()
    permissions_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        company = self.request.user.employee.company_id
        queryset = self.queryset.filter(ads__campaign__company_id=company)

        ad_id = self.request.query_params.get('ad_id', None)
        if ad_id:
            queryset = queryset.filter(ads_id=ad_id)

        return queryset

    def list(self, request, *args, **kwargs):
        self.queryset = self.get_queryset()

        return super().list(request, *args, **kwargs)


class ImpressionViewSet(viewsets.ModelViewSet):
    serializer_class = ImpressionSerializer
    permissions_classes = (permissions.IsAuthenticated,)
    queryset = Impression.objects.all()

    def get_queryset(self):
        company = self.request.user.employee.company_id
        queryset = self.queryset.filter(ads__campaign__company_id=company)

        ad_id = self.request.query_params.get('ad_id', None)
        if ad_id:
            queryset = queryset.filter(ads_id=ad_id)

        return queryset

    def list(self, request, *args, **kwargs):
        self.queryset = self.get_queryset()

        return super().list(request, *args, **kwargs)
