from django.contrib.gis.db import models

# Create your models here.
class State(models.Model):
    region = models.CharField(max_length=2)
    division = models.CharField(max_length=2)
    statefp = models.CharField(max_length=2)
    statens = models.CharField(max_length=8)
    geoid = models.CharField(max_length=2)
    stusps = models.CharField(max_length=2)
    name = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    funcstat = models.CharField(max_length=1)
    aland = models.BigIntegerField()
    awater = models.BigIntegerField()
    intptlat = models.CharField(max_length=11)
    intptlon = models.CharField(max_length=12)
    geom = models.MultiPolygonField(srid=4269)

    def __str__(self):
        return self.name
