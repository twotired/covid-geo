# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiger', '0001_initial'),
        ('uscensus', '0001_initial'),
    ]

    sql = """
    create VIEW county_info as
    SELECT tc.geoid,
       ts.name AS state,
       tc.name AS county,
       tc.statefp,
       tc.countyfp,
       p.census2010pop,
       p.popestimate2019
      FROM tiger_county tc
        JOIN ( select
               uscensus_population.state,
               uscensus_population.county,
               uscensus_population.census2010pop,
               uscensus_population.popestimate2019
              FROM uscensus_population
             WHERE uscensus_population.county > 0) p ON (p.state = tc.statefp and p.county = tc.countyfp)
        JOIN tiger_state ts ON (ts.statefp = tc.statefp)
        order by state,county
    """

    operations = [
        migrations.RunSQL("drop view if exists county_info;"),
        migrations.RunSQL(sql)
    ]
