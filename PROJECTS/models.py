from django.db import models

# Create your models here.


class Proiect (models.Model):

	nume=models.CharField(max_length=30,unique=True)
	id_proiect=models.IntegerField(unique=True)
	descriere=models.CharField(max_length=100)



	def __str__(self):
		return self.nume

