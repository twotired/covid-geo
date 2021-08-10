from django.db import models

# Create your models here.

class US(models.Model):
    date = models.DateField(null=False, primary_key=True)
    cases = models.BigIntegerField(null=False)
    deaths = models.BigIntegerField(null=False)

    class Meta:
        verbose_name_plural = 'US'

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")

# \copy nytcoviddata_us from 'us.csv' header csv;

class State(models.Model):
    date = models.DateField(null=False)
    state = models.CharField(max_length=32)
    fips = models.IntegerField()
    cases = models.BigIntegerField(null=False)
    deaths = models.BigIntegerField(null=False)

    class Meta:
        unique_together = [['date', 'state']]

    def __str__(self):
        return "%s %s" % (self.state, self.date.strftime("%Y-%m-%d"))

# \copy nytcoviddata_state (date,state,fips,cases,deaths) from 'us-states.csv' with (format csv, header true);

class County(models.Model):
    date = models.DateField(null=False)
    county = models.CharField(max_length=128) # can be 'Unknown'
    state = models.CharField(max_length=32)
    fips = models.IntegerField(null=True)     # can be 0
    cases = models.BigIntegerField(null=False)
    deaths = models.BigIntegerField(null=True)

    class Meta:
        unique_together = [['date', 'state', 'fips']]
        verbose_name_plural = 'Counties'

    def __str__(self):
        return "%s %s %s" % (self.state, self.county, self.date.strftime("%Y-%m-%d"))

# \copy nytcoviddata_county (date,county,state,fips,cases,deaths) from 'us-counties.csv' with (format csv, header true);
