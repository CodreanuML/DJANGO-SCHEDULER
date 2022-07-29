from django.shortcuts import render,redirect
from .models import Proiect
from EVENTS.models import Eveniment_Template,Eveniment
from .forms import Proiect_ADD
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from ACCOUNTS.models import Employee
# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required
def home(request):

	user_req = request.user
	employee_req=Employee.objects.get(user=user_req)
	proiecte_querry_req=Proiect.objects.all()


	paginator = Paginator(proiecte_querry_req, 25) 

	page_number = request.GET.get('page')
	proiecte_querry = paginator.get_page(page_number)
   


	evenimente_q=Eveniment.objects.filter(responsabil=user_req,status=False)


	return render(request,'PROJECTS/home.html',{'proiecte_querry':proiecte_querry,'employee':employee_req,'queue_tasks':evenimente_q})


@login_required
def new_project(request):
	if request.method=="POST":
		form=Proiect_ADD(request.POST)
		if form.is_valid():
			form.save()
			return redirect('PROJECTS:projects_home')
	else:
		form=Proiect_ADD()
	return render(request,'PROJECTS/proiectnou.html',{'form':form})


@login_required
def project_details(request,pk):
	proiect_querry=Proiect.objects.get(pk=pk)
	eveniment_template_querry_req=Eveniment_Template.objects.filter(proiect=proiect_querry)



	paginator = Paginator(eveniment_template_querry_req, 20)

	page_number = request.GET.get('page')
	eveniment_template_querry = paginator.get_page(page_number)


	return render(request,'PROJECTS/proiect_detalii.html',{'proiect':proiect_querry,'eveniment_template':eveniment_template_querry})


