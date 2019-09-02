from django.db import models
from sorl.thumbnail import ImageField
from embed_video.fields import EmbedVideoField

# Create your models here.
class Rating(models.Model):
	tittle = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return self.tittle	

class Genre(models.Model):
	tittle = models.CharField(max_length=200)

	def __str__(self):
		return self.tittle

class Studio(models.Model):
	tittle = models.CharField(max_length=200)

	def __str__(self):
		return self.tittle	

class Movie(models.Model):
	tittle = models.CharField(max_length=200)
	image = ImageField(upload_to='whatever')
	description = models.TextField()
	rating = models.ForeignKey(Rating,on_delete=models.DO_NOTHING)
	genre = models.ForeignKey(Genre,on_delete=models.DO_NOTHING)
	directed_by = models.CharField(max_length=200)
	written_by = models.CharField(max_length=200)
	in_theaters = models.DateField()
	runtime = models.CharField(max_length=200)
	studio = models.ForeignKey(Studio,on_delete=models.DO_NOTHING)
	video = EmbedVideoField()

	def __str__(self):
		return self.tittle
