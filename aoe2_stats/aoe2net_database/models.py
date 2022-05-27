from django.db import models

# Create your models here.

class PlayerMatchStat(models.Model):

    civ = models.CharField(max_length=80)
    civ_id = models.IntegerField()