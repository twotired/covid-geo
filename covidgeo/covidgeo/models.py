from django.contrib.gis.db import models

class CountyInfo(models.Model):
    geoid = models.IntegerField()
    state = models.CharField(max_length=128)
    county = models.CharField(max_length=256)
    statefp = models.IntegerField()
    countyfp = models.IntegerField()
    census2010pop = models.IntegerField()
    popestimate2019 = models.IntegerField()

    class Meta:
        verbose_name_plural = 'CountiesInfo'
        managed = False
