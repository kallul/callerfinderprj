from django.db import models

# Create your models here.
class Truecaller(models.Model):
    name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=15)
    access_token = models.CharField(max_length=80)
    requestId = models.CharField(max_length=80)