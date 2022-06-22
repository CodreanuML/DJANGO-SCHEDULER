from django import forms
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm 
from django.contrib.auth.models import User

from .models import Employee 









class RegistrationForm(UserCreationForm):
    

    DEP_CHOICES = [
        ('Productie', 'Productie'),
        ('Mentenanta', 'Mentenanta'),
       
    ]


    ZONA_CHOICES = [
        ('Asamblare', 'Asamblare'),
        ('Airbag', 'Airbag'),
        ('Foaming' , 'Foaming'),
        ('Diecasting' , 'Diecasting'),
        ('LW' , 'LW'),
        ('IMO' , 'IMO'),
        ('Toolshop' , 'Toolshop'),
        ('Toate' , 'Toate'),

    ]

   
    department = forms.ChoiceField(choices=DEP_CHOICES,label='Selectati departamentul')
    Zona = forms.ChoiceField(choices=ZONA_CHOICES,label='Selectati aria')




    class Meta: 
        model = User
        fields = (
            'username', 'password1', 'password2' ,
            'department',
            'Zona',


        )
        labels = {
        'username': ('Utilizator'),
        'password1': ('Parola'),
        'password2': ('Repeta Parola'),
        'department': ('Selectati departamentu'),
        'Zona': ('Selectati aria'),
        }
        
