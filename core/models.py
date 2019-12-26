from django.db import models

# Create your models here.
class Bucket(models.Model):
	title = models.CharField(max_length=120)
	movie = models.CharField(max_length=120)
	romance = models.CharField(max_length=120)
	action = models.CharField(max_length=120)
