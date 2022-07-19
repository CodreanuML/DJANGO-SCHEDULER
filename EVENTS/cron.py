from .models import Eveniment_Template,Eveniment
from django.contrib.auth.models import User
import datetime

from datetime import timedelta






#GENEREAZA EVENIMENTE AUTOMAT EVENIMENTE

def scan_template_generate_events():


  

#Selectam Toate Templateurile

  Eveniment_Template_querry=Eveniment_Template.objects.all()

#Initializam fiecare Template

  for Eveniment_Template_instance in Eveniment_Template_querry  :

#Verificam daca statusul templateului este activ
    if Eveniment_Template_instance.status==True :  

      anul_curent=datetime.date.today().year
      luna_curenta=datetime.date.today().month
      ziua_curenta=datetime.date.today().day

      template_anul_curent=Eveniment_Template_instance.an_incepere
      template_luna_curenta=Eveniment_Template_instance.luna_incepere
      template_ziua_curenta=Eveniment_Template_instance.zi_incepere

#Verificam data de incepere >  data actuala 

      if (anul_curent>=template_anul_curent and  luna_curenta>=template_luna_curenta and ziua_curenta>=template_ziua_curenta ):

#Selectam respomsabilul de actiune
        Eveniment_Template_instance.responsabil
#Cautam ultima data de executie
        Evenimente_querry=Eveniment.objects.filter(eveniment_template=Eveniment_Template_instance).order_by('-data_initiere')

        Eveniment_querry_last=Evenimente_querry[0]
#Verificam daca recurenta a fost depasita si daca da instantiem o noua instanta
        
        if Eveniment_querry_last != None :
          data_verificare=Eveniment_querry_last.data_initiere+timedelta(days=+Eveniment_Template_instance.recurenenta_zile)


    

          if data_verificare == datetime.date.today():

#Creaza o instanta noua utilizand data celei precedente
            Eveniment.objects.create(responsabil=User_querry,eveniment_template=Eveniment_Template_instance,data_initiere=datetime.date.today(),data_finalizare=datetime.date.today()+timedelta(days=+Eveniment_Template_instance.zile_executie),status=False)
        else :
#Creaza o instanta noua daca nu exista
          Eveniment.objects.create(responsabil=User_querry,eveniment_template=Eveniment_Template_instance,data_initiere=datetime.date.today(),data_finalizare=datetime.date.today()+timedelta(days=+Eveniment_Template_instance.zile_executie),status=False)






#VERIFICA DACA TREBUIE INCHIS AUTOMAT EVENIMENTE

def scan_events_to_close_status():
  
  Eveniment_Template_querry=Eveniment_Template.objects.all()

#Initializam fiecare Template

  for Eveniment_Template_instance in Eveniment_Template_querry  :

#Verificam daca statusul templateului este activ
    if Eveniment_Template_instance.status==True :  

      Evenimente_querry=Eveniment.objects.filter(eveniment_template=Eveniment_Template_instance).order_by('-data_initiere')

      Eveniment_querry_last=Evenimente_querry[0]

      if Eveniment_querry_last.status==False: 

        data_inchidere=Eveniment_querry_last.data_initiere+timedelta(days=+Eveniment_Template_instance.zile_executie)

        if data_inchidere <= datetime.date.today():

          Eveniment_querry_last.status=True

          Eveniment_querry_last.save()


