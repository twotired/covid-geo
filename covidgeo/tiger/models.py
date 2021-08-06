from django.contrib.gis.db import models

# Create your models here.
class State(models.Model):
    region = models.CharField(max_length=2, help_text='region code')
    division = models.CharField(max_length=2, help_text='division code')
    statefp = models.CharField(max_length=2, help_text='state FIPS code')
    statens = models.CharField(max_length=8, help_text='ANSI feature code for the state or equivalent entity')
    geoid = models.CharField(max_length=2, help_text='State identifier; state FIPS code')
    stusps = models.CharField(max_length=2,
                                primary_key=True,
                                help_text='United States Postal Service state abbreviation')
    name = models.CharField(max_length=100, help_text='state name')
    lsad = models.CharField(max_length=2, help_text='legal/statistical area description code for state')
    mtfcc = models.CharField(max_length=5, help_text='MAF/TIGER Feature Class Code (G4000)')
    funcstat = models.CharField(max_length=1, help_text='functional status')
    aland = models.BigIntegerField(help_text='land area')
    awater = models.BigIntegerField(help_text='water area')
    intptlat = models.CharField(max_length=11, help_text='latitude of the internal point')
    intptlon = models.CharField(max_length=12, help_text='longitude of the internal point')
    geom = models.MultiPolygonField(srid=4269)

    def __str__(self):
        return self.name

# manage.py ogrinspect --mapping --multi tl_2020_us_county.shp County
class County(models.Model):
    statefp = models.CharField(max_length=2, help_text='state FIPS code')
    countyfp = models.CharField(max_length=3, help_text='county FIPS code')
    countyns = models.CharField(max_length=8, help_text='ANSI feature code for the county or equivalent feature')
    geoid = models.CharField(max_length=5, help_text='County identifier; a concatenation of Current state FIPS code and county FIPS code')
    name = models.CharField(max_length=100, help_text='county name')
    namelsad = models.CharField(max_length=100, help_text='name and the translated legal/statistical area description for county')
    lsad = models.CharField(max_length=2, help_text='legal/statistical area description code for county')
    classfp = models.CharField(max_length=2, help_text='FIPS class code')
    mtfcc = models.CharField(max_length=5, help_text='MAF/TIGER Feature Class Code (G4020)')
    csafp = models.CharField(max_length=3, null=True, help_text='combined statistical area code')
    cbsafp = models.CharField(max_length=5, null=True, help_text='metropolitan statistical area/micropolitan statistical area code')
    metdivfp = models.CharField(max_length=5, null=True, help_text='metropolitan division code')
    funcstat = models.CharField(max_length=1, help_text='functional status')
    aland = models.BigIntegerField(help_text='land area')
    awater = models.BigIntegerField(help_text='water area')
    intptlat = models.CharField(max_length=11, help_text='latitude of the internal point')
    intptlon = models.CharField(max_length=12, help_text='longitude of the internal point')
    geom = models.MultiPolygonField(srid=4269)

    class Meta:
        verbose_name_plural = 'Counties'

    def __str__(self):
        return self.namelsad

# manage.py ogrinspect --mapping --multi tl_2020_us_uac10.shp UrbanArea
class UrbanArea(models.Model):
    uace10 = models.CharField(max_length=5, help_text='2010 Census urban area code')
    geoid10 = models.CharField(max_length=5, help_text='2010 Census urban area identifier; 2010 Census urban area code')
    name10 = models.CharField(max_length=100, help_text='2010 Census urban area name')
    namelsad10 = models.CharField(max_length=100, help_text='2010 Census name and the translated legal/statistical area description for urban area')
    lsad10 = models.CharField(max_length=2, help_text='2010 Census legal/statistical area description code for urban area')
    mtfcc10 = models.CharField(max_length=5, help_text='MAF/TIGER Feature Class Code (G3500)')
    uatyp10 = models.CharField(max_length=1, help_text='2010 Census urban area type')
    funcstat10 = models.CharField(max_length=1, help_text='2010 Census functional status')
    aland10 = models.BigIntegerField(help_text='2010 Census land area')
    awater10 = models.BigIntegerField(help_text='2010 Census water area')
    intptlat10 = models.CharField(max_length=11, help_text='2010 Census latitude of the internal point')
    intptlon10 = models.CharField(max_length=12, help_text='2010 Census longitude of the internal point')
    geom = models.MultiPolygonField(srid=4269)

    class Meta:
        verbose_name_plural = 'Urban Areas'

    def __str__(self):
        return self.name10

# manage.py ogrinspect --mapping --multi tl_2020_us_cd116.shp CongressionalDistrict
class CongressionalDistrict(models.Model):
    statefp = models.CharField(max_length=2, help_text='state FIPS code')
    cd116fp = models.CharField(max_length=2, help_text='116th congressional district FIPS code')
    geoid = models.CharField(max_length=4, help_text='116th congressional district identifier; a concatenation of current state FIPS code and the 116th congressional district FIPS code')
    namelsad = models.CharField(max_length=41, help_text='name and the translated legal/statistical area description for congressional district')
    lsad = models.CharField(max_length=2, help_text='legal/statistical area description code for congressional district')
    cdsessn = models.CharField(max_length=3, help_text='Congressional session code')
    mtfcc = models.CharField(max_length=5, help_text='MAF/TIGER Feature Class Code (G5200)')
    funcstat = models.CharField(max_length=1, help_text='Current functional status')
    aland = models.BigIntegerField(help_text='land area')
    awater = models.BigIntegerField(help_text='water area')
    intptlat = models.CharField(max_length=11, help_text='latitude of the internal point')
    intptlon = models.CharField(max_length=12, help_text='longitude of the internal point')
    geom = models.MultiPolygonField(srid=4269)

    def __str__(self):
        return self.namelsad
