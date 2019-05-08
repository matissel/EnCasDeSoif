from django.db import models
from django.contrib.auth.models import User


class PointEau(models.Model):
    nom = models.CharField(blank=False, default='Name', max_length=100)
    long = models.FloatField()
    lat = models.FloatField()
    desc = models.CharField(blank=False, default='Description', max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '''--Point eau --
            \r\tID : {0}
            \r\tNom : {1}
            \r\tLongitude: {2}
            \r\tLatitude:{3}
            \r\tDesc : {4}
            \r\tOwner : {5}\n'''.format(self.id, self.nom, self.long, self.lat, self.desc, self.owner)
