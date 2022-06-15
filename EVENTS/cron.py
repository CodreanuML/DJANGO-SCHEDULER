from .models import Eveniment_Template,Eveniment
from django.contrib.auth.models import User
import datetime

from datetime import timedelta




""" VERIFICA DACA ESTE NEVOIE SA GENEREZE UN NOU EVENIMENT"""


def my_scheduled_job():


  User_querry=User.objects.get(username='codreanuml')



  Eveniment_Template_querry=Eveniment_Template.objects.all()


  for Eveniment_Template_instance in Eveniment_Template_querry  :

    

    Evenimente_querry=Eveniment.objects.filter(eveniment_template=Eveniment_Template_instance).order_by('-data_initiere')

    Eveniment_querry_last=Evenimente_querry[0]

    Eveniment_Template_instance.recurenenta_zile

    data_verificare=Eveniment_querry_last.data_initiere+timedelta(days=+Eveniment_Template_instance.recurenenta_zile)


    if data_verificare == datetime.date.today():


      Eveniment.objects.create(responsabil=User_querry,eveniment_template=Eveniment_Template_instance,data_initiere=datetime.date.today(),data_finalizare=datetime.date.today(),status=False)