from django.db import models

# Create your models here.

class Branch(models.Model):
	name 	= models.CharField(max_length=220)
	pno  	= models.CharField(max_length=10)
	address = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name


class NewsPaper(models.Model):
	name 		= models.CharField(max_length=120)
	price 		= models.IntegerField()
	image		= models.ImageField()
	language 	= models.CharField(max_length=100,default="Telugu")

	def __str__(self):
		return self.name

magazine_choices=(
		('weekly','weekly'),
		('monthly','monthly'),
	)
class Magazine(models.Model):
	name 			= models.CharField(max_length=120)
	price 			= models.IntegerField()
	magazine_type 	= models.CharField(max_length=10,choices=magazine_choices)
	language 	= models.CharField(max_length=100,default="Telugu")
	image			= models.ImageField()

	def __str__(self):
		return self.name
