from django.db import migrations

class Migration(migrations.Migration):

  dependencies = [
      ('ad_analytics', '0014_backfill'),
  ]

  operations = [
      # Django considers "id" the primary key of these tables, but
      # we want the primary key to be (account_id, id)
      migrations.RunSQL("""
      ALTER TABLE ad_analytics_campaign
      DROP CONSTRAINT ad_analytics_campaign_pkey CASCADE;
 
      ALTER TABLE ad_analytics_campaign
      ADD CONSTRAINT ad_analytics_campaign_pkey
      PRIMARY KEY (company_id, id)
      """),

      migrations.RunSQL("""
      ALTER TABLE ad_analytics_ads
      DROP CONSTRAINT ad_analytics_ads_pkey CASCADE;

      ALTER TABLE ad_analytics_ads
      ADD CONSTRAINT ad_analytics_ads_pkey
      PRIMARY KEY (company_id, id)
      """),

      migrations.RunSQL("""
      ALTER TABLE ad_analytics_click
      DROP CONSTRAINT ad_analytics_click_pkey CASCADE;

      ALTER TABLE ad_analytics_click
      ADD CONSTRAINT ad_analytics_click_pkey
      PRIMARY KEY (company_id, id)
      """),

      migrations.RunSQL("""
      ALTER TABLE ad_analytics_impression
      DROP CONSTRAINT ad_analytics_impression_pkey CASCADE;

      ALTER TABLE ad_analytics_impression
      ADD CONSTRAINT ad_analytics_impression_pkey
      PRIMARY KEY (company_id, id)
      """),

      migrations.RunSQL("""
      ALTER TABLE ad_analytics_campaign_collaborators
      DROP CONSTRAINT ad_analytics_campaign_collaborators_pkey CASCADE;

      ALTER TABLE ad_analytics_campaign_collaborators
      ADD CONSTRAINT ad_analytics_campaign_collaborators_pkey
      PRIMARY KEY (company_id, id)
      """),

      migrations.RunSQL("""
      ALTER TABLE ad_analytics_employee
      DROP CONSTRAINT ad_analytics_employee_pkey CASCADE;

      ALTER TABLE ad_analytics_employee
      ADD CONSTRAINT ad_analytics_employee_pkey
      PRIMARY KEY (company_id, id)
      """),


  ]
