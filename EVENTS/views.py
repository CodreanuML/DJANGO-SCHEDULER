from django.shortcuts import render,redirect,reverse
from .models import Eveniment_Template ,Eveniment
from PROJECTS.models import Proiect
from  .forms import Eveniment_Template_form
import datetime
# Create your views here.


def home(request,proiect_pk) :
	proiect_querry=Proiect.objects.get(pk=proiect_pk)
	eveniment_template_querry=Eveniment_Template.objects.filter(proiect=proiect_querry)
	return render(request,'EVENTS/home.html',{'proiect':proiect_querry,'eveniment_template':eveniment_template_querry})



def eveniment_template_nou(request,proiect_pk):
	proiect_querry=Proiect.objects.get(pk=proiect_pk)	

	


	if request.method=="POST":
		
		form=Eveniment_Template_form(request.POST)
		if form.is_valid():

			eveniment_template=form.save(commit=False)


			if form.cleaned_data['recurenenta']=='saptamanal':
				eveniment_template.recurenenta_zile=7
				
			elif form.cleaned_data['recurenenta']=='lunar':
				eveniment_template.recurenenta_zile=28
				
			elif form.cleaned_data['recurenenta']=='anual':
				eveniment_template.recurenenta_zile=336
				
			elif form.cleaned_data['recurenenta'] =='2ani':
				eveniment_template.recurenenta_zile=672
			
			an=form.cleaned_data['an_incepere']
			luna=form.cleaned_data['luna_incepere']
			zi=form.cleaned_data['zi_incepere']

			eveniment_template.data_initiere=datetime.date(an,luna,zi)

			eveniment_template.save()

			
			return redirect('PROJECTS:projects_home')
	else :

		form=Eveniment_Template_form()


	return render(request,'EVENTS/eveniment_template_nou.html',{'form':form})



def detalii_eveniment_template(request,eveniment_pk):
	eveniment_querry=Eveniment_Template.objects.get(pk=eveniment_pk)



	return render(request,'EVENTS/datalii_eveniment_template.html',{'eveniment':eveniment_querry})



def istoric_evenimente(request,eveniment_pk):
	eveniment_template_querry=Eveniment_Template.objects.get(pk=eveniment_pk)
	eveniment_querry=Eveniment.objects.filter(eveniment_template=eveniment_template_querry)


	return render(request ,'EVENTS/istoric_evenimente.html',{'eveniment_q':eveniment_querry})



def finalizeaza_eveniment(request,eveniment_pk):
	eveniment_querry=Eveniment.objects.get(pk=eveniment_pk)

	eveniment_querry.data_finalizare=datetime.date.today()

	eveniment_querry.status=1

	eveniment_querry.save()

	return redirect('PROJECTS:projects_home')



	