from django.db import models

class PointEau(models.Model):
    nom = models.CharField(blank=False, default='Name',max_length=100)
    long = models.FloatField()
    lat = models.FloatField()
    desc = models.CharField(blank=False,default='Description', max_length=255)
    def __str__(self):
        return '%s %s %s %s' % (self.nom, self.long, self.lat, self.desc)
