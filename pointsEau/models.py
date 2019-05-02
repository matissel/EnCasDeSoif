from django.db import models

class PointEau(models.Model):
    nom = models.CharField(blank=False, default='Name',max_length=100)
    long = models.FloatField()
    lat = models.FloatField()

