from django.db import models

# Create your models here.

# https://www2.census.gov/programs-surveys/popest/datasets/2010-2020/counties/totals/
class Population(models.Model):
    sumlev = models.IntegerField()
    region = models.IntegerField()
    division = models.IntegerField()
    state = models.IntegerField()
    county = models.IntegerField()
    stname = models.CharField(max_length=128)
    ctyname = models.CharField(max_length=128)
    census2010pop = models.IntegerField(null=True)
    estimatesbase2010 = models.IntegerField()
    popestimate2010 = models.IntegerField()
    popestimate2011 = models.IntegerField()
    popestimate2012 = models.IntegerField()
    popestimate2013 = models.IntegerField()
    popestimate2014 = models.IntegerField()
    popestimate2015 = models.IntegerField()
    popestimate2016 = models.IntegerField()
    popestimate2017 = models.IntegerField()
    popestimate2018 = models.IntegerField()
    popestimate2019 = models.IntegerField()
    popestimate042020 = models.IntegerField()
    popestimate2020 = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Population'
        unique_together = [['state', 'county']]
