from django.db import models

# Create your models here.

class Digimon(models.Model):
    name = models.CharField(max_length=50)
    img = models.URLField()
    level = models.CharField(max_length=50)
    
    def __str__(self) :
        return self.name