from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Operator(models.Model):
    faction = models.CharField(max_length=100)
    skin = models.CharField(max_length=100)
    camo = models.CharField(max_length=100)
    unlock = models.TextField()
    image = models.ImageField(upload_to="game/", blank=True, null=True)
 
    def __str__(self):
        return self.skin 