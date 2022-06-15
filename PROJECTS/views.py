from django.shortcuts import render,redirect
from .models import Proiect
from EVENTS.models import Eveniment_Template
from .forms import Proiect_ADD
# Create your views here.


def home(request):
	proiecte_querry=Proiect.objects.all()
	return render(request,'PROJECTS/home.html',{'proiecte_querry':proiecte_querry})



def new_project(request):
	if request.method=="POST":
		form=Proiect_ADD(request.POST)
		if form.is_valid():
			form.save()
			return redirect('PROJECTS:projects_home')
	else:
		form=Proiect_ADD()
	return render(request,'PROJECTS/proiectnou.html',{'form':form})



def project_details(request,pk):
	proiect_querry=Proiect.objects.get(pk=pk)
	eveniment_template_querry=Eveniment_Template.objects.filter(proiect=proiect_querry)

	return render(request,'PROJECTS/proiect_detalii.html',{'proiect':proiect_querry,'eveniment_template':eveniment_template_querry})