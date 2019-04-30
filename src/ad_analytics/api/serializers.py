from rest_framework import serializers

from ad_analytics.models import *



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Company


class CampaignSerializer(serializers.ModelSerializer):
    state = serializers.SerializerMethodField()

    class Meta:
        model = Campaign
        fields = '__all__'
        read_only_fields = ('conpany')
        depth = 1

    def get_state(self, obj):
        return obj.get_state_display()


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ('name', 'campaign', 'impressions_count', 'clicks_count', 'created_at')
        depth = 1


class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('ads', 'site_url', 'cost_per_click_usd', 'user_ip', 'clicked_at')
        model = Click


class ImpressionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Impression
