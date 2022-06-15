from django import forms
from PROJECTS.models import Proiect

class Proiect_ADD(forms.ModelForm):
	nume=forms.CharField(max_length=30,label='Introduceti numele Proiectului',widget=forms.TextInput(attrs={'placeholder':'Nume Proiect'}))
	id_proiect=forms.IntegerField(label='ID inregistrare Proiect',widget=forms.NumberInput(attrs={'placeholder':'ID Proiect'}))
	descriere=forms.CharField(max_length=100,label='Descirerea Proiectului',widget=forms.TextInput(attrs={'placeholder':'Descriere Proiect'}))


	class Meta :
		model=Proiect
		fields=['nume','id_proiect','descriere']