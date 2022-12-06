from django.db import models

# Create your models here.

class Bay(models.Model):
    bay_number= models.IntegerField()
    status = models.CharField(max_length=100,default="Free")