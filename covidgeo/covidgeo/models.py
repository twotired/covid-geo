from django.contrib.gis.db import models

class StateInfo(models.Model):
    geoid = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=128)
    statefp = models.IntegerField()
    census2010pop = models.IntegerField()
    popestimate2019 = models.IntegerField()

class CountyInfo(models.Model):
    geoid = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=128)
    county = models.CharField(max_length=256)
    statefp = models.IntegerField()
    countyfp = models.IntegerField()
    census2010pop = models.IntegerField()
    popestimate2019 = models.IntegerField()

    class Meta:
        verbose_name_plural = 'CountiesInfo'
        managed = False
        db_table = 'county_info'

class CountyCovid(models.Model):
    id = models.BigIntegerField(primary_key=True, null=False)
    date = models.DateField(null=False)
    county = models.CharField(max_length=128, null=False)
    state = models.CharField(max_length=32, null=False)
    fips = models.IntegerField(null=False)
    cases = models.IntegerField(null=False)
    deaths = models.IntegerField(null=False)
