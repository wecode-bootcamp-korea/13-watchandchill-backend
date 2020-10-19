from django.db import models

class Movies(models.Model):
	title		= models.CharField(Max_length=100)
	poster_url	= models.CharField(Max_length=100)