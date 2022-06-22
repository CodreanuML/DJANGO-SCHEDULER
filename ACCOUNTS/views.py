from django.contrib.auth import login 
from django.shortcuts import render, redirect
from .forms import  RegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Employee
from django.http import HttpResponse , request



from django.contrib import messages






def home(request):

    return render(request,'ACCOUNTS/home.html')





def signup(request):

	if request.method=='POST':
		form=RegistrationForm(request.POST)
		if form.is_valid():
			new_user=form.save()
			new_user_name=form.cleaned_data['username']
			employee_department=form.cleaned_data['department']
			employee_zona=form.cleaned_data['Zona']
			Employee_enq=Employee.objects.create(user=new_user,department=employee_department,Zona=employee_zona)
			Employee_enq.save()
			messages.success(request,'Inregistrare utilizator cu success : ' +str(new_user_name) )
		else:
			messages.success(request,'Utilizatorul nu a fost inregistrat, a aparut o eroare.Verificati Numele si Parola.' )
		return redirect('PROJECTS:projects_home')

	else:


		form=RegistrationForm()
	return render(request,'ACCOUNTS/signup.html',{'form':form})