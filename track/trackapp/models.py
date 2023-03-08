from django.db import models

# Create your models here.
class Loc(models.Model):
    latitude = models.CharField(max_length=120)
    longitude = models.CharField(max_length=120)

    def __str__(self):
        return self.latitude,self.longitude