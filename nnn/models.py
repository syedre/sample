from django.db import models

#reate your models here.
class Proo(models.Model):
	name = models.CharField(max_length=120)
	descrip = models.CharField(max_length=120)
	dindong = models.CharField(max_length=120)
	hhgh = models.CharField(max_length=120,default='hvhvhbh jgj')
	real = models.TextField(max_length=120,default=' tgfgf null')

	
