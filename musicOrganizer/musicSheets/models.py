from django.db import models

# Create your models here.

class sheetMusic(models.Model):
	title = models.CharField(max_length=300)
	composer = models.CharField(max_length=300)
	difficulty = models.CharField(max_length=50)
	location = models.CharField(max_length=200)

