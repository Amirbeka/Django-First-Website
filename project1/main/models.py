from django.db import models

class Ism(models.Model):
    ism = models.CharField(max_length=40)
    familiya = models.CharField(max_length=40)
    ty = models.IntegerField()
    