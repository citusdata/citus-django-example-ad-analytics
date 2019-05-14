from django.db import migrations

class Migration(migrations.Migration):

  dependencies = [
    ('ad_analytics', '0013_add_company_manytomany'),
  ]

  operations = [
    migrations.RunSQL("""
      UPDATE ad_analytics_ads
      SET company_id = campaigns.company_id
      FROM ad_analytics_campaign campaigns
      WHERE campaigns.id = ad_analytics_ads.campaign_id;
    """),

    migrations.RunSQL("""
      UPDATE ad_analytics_click
      SET company_id = ads.company_id
      FROM ad_analytics_ads ads
      WHERE ads.id = ad_analytics_click.ads_id;
    """),

    migrations.RunSQL("""
      UPDATE ad_analytics_impression
      SET company_id = ads.company_id
      FROM ad_analytics_ads ads
      WHERE ads.id = ad_analytics_impression.ads_id;
    """),

    migrations.RunSQL("""
      UPDATE ad_analytics_campaign_collaborators
      SET company_id = campaigns.company_id
      FROM ad_analytics_campaign campaigns
      WHERE campaigns.id = ad_analytics_campaign_collaborators.campaign_id;
    """),

  ]
