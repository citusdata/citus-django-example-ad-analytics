from django.db import migrations

class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('ad_analytics', '0012_auto_20190524_2259'),
    ]

    operations = [
        migrations.RunSQL("""
        ALTER TABLE ad_analytics_campaign_collaborators DROP CONSTRAINT ad_analytics_campaign_co_campaign_id_employee_id_bc477b48_uniq;
        """),

        migrations.RunSQL("""
        CREATE UNIQUE INDEX ad_analytics_campaign_co_campaign_id_employee_id_bc477b48_uniq ON ad_analytics_campaign_collaborators (company_id, campaign_id, employee_id);
        """),

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
