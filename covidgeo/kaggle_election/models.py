from django.db import models

# Create your models here.
class PresidentCounty2020(models.Model):
    state = models.CharField(max_length=32)
    county = models.CharField(max_length=128)
    candidate = models.CharField(max_length=128)
    party = models.CharField(max_length=128)
    total_votes = models.IntegerField()
    won = models.BooleanField()

    class Meta:
        unique_together = [['state', 'county', 'candidate']]
