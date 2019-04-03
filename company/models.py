from django.db import models
from django.conf import settings

# Create your models here.
class Company(models.Model):
	name = models.CharField(max_length=250)
	phone_number = models.CharField(max_length=15)
	address = models.TextField(blank=True, null=True)