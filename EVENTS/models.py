from django.db import models
from PROJECTS.models import Proiect
# Create your models here.
from django.contrib.auth.models import User


class Eveniment_Template(models.Model):
	nume = models.CharField(max_length=100)
	
	proiect=models.ForeignKey(Proiect,related_name='evenimente',on_delete=models.CASCADE,null=True, blank=True)
	responsabil=models.ForeignKey(User,related_name='eveniment_temp',on_delete=models.CASCADE)
	activitati_necesare=models.TextField(max_length=300)
 
	CHOICES=[('saptamanal', 'saptamanal') , ('lunar','lunar') , ('anual','anual') , ('2ani','2ani') ]

	recurenenta=models.CharField(choices=CHOICES,max_length=100)

	recurenenta_zile=models.IntegerField()

	zile_executie=models.IntegerField()

	

	an_choice=[(2022,2022),(2023,2023),(2024,2024),(2025,2025),(2026,2026),]
	luna_choice=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12)]
	zi_choice=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12),(13,13),(14,14),(15,15),(16,16),(17,17),(18,18),(19,19),(20,20),(21,21),(22,22),(23,23),(24,24),(25,25),(26,26),(27,27),(28,28)]
	
	an_incepere=models.IntegerField(choices=an_choice)
	luna_incepere=models.IntegerField(choices=luna_choice)
	zi_incepere=models.IntegerField(choices=zi_choice)

	data_initiere=models.DateField(null=True)

	status=models.BooleanField()

	def __str__(self):
		return self.nume




 
class Eveniment(models.Model):
	responsabil=models.ForeignKey(User,related_name='eveniment_inst',on_delete=models.CASCADE)
	eveniment_template=models.ForeignKey(Eveniment_Template,related_name='eveniment_obj',on_delete=models.CASCADE)
	data_initiere=models.DateField()
	data_finalizare=models.DateField(blank=True)
	status=models.BooleanField() # 1 deschis si nefinalizat 2 deschis si finalizat 

	
	def __str__(self):
		return str(self.eveniment_template.nume +" - Raport ID :" +str(self.pk))


	class Meta :
		ordering=['data_finalizare']