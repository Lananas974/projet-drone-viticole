from django.db import models

# Create your models here.

class Drone(models.Model):
    nom = models.CharField(max_length=100)
    vitesse = models.FloatField(default=0.0) # en km/h
    altitude = models.FloatField(default=0.0) # en mètres
    batterie = models.IntegerField(default=100) # pourcentage
    est_actif = models.BooleanField(default=False)

    def __str__(self):
        return self.nom
 