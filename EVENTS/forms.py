from django import forms
from .models import Eveniment_Template
from PROJECTS.models import Proiect


class Eveniment_Template_form(forms.ModelForm):
	nume=forms.CharField(max_length=100)
	
	
	CHOICES=[('saptamanal', 'saptamanal') , ('lunar','lunar') , ('anual','anual') , ('2ani','2ani') ]
	recurenenta=forms.ChoiceField(choices=CHOICES)
	

	class Meta:
		model=Eveniment_Template
		fields=['nume','proiect','responsabil','activitati_necesare','recurenenta','zile_executie','an_incepere','luna_incepere','zi_incepere','status']
		label=['Nume Eveniment','Proiect','Responsabil','Activitati','Recurenta','Zile incheiere activitate','Anul inceperii activitatii','Luna inceperii activitatii','Ziua inceperii activitatii','Starea ordinului']