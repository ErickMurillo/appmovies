from django.db import models
from movies.models import *
from django.contrib.auth.models import User

# Create your models here.
STAR_CHOICES = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))

class Review(models.Model):
	user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	movie = models.ForeignKey(Movie,on_delete=models.DO_NOTHING)
	review = models.TextField()
	stars = models.IntegerField(choices=STAR_CHOICES)