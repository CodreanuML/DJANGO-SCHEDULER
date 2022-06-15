from django.urls import include, path

app_name = "EVENTS"

from . import views as EVENTS_VIEWS

urlpatterns = [ path('proiect/<int:proiect_pk>/',EVENTS_VIEWS.home,name='events_home' ),
				path('proiect/<int:proiect_pk>/template/',EVENTS_VIEWS.eveniment_template_nou,name='eveniment_template_nou'),
				path('eveniment_template/<int:eveniment_pk>/',EVENTS_VIEWS.detalii_eveniment_template,name='detalii_eveniment_template'),
				path('eveniment_template/<int:eveniment_pk>/istoric_evenimente/',EVENTS_VIEWS.istoric_evenimente,name='istoric_evenimente'),
				path('eveniment_template/<int:eveniment_pk>/finalizeaza_eveniment/',EVENTS_VIEWS.finalizeaza_eveniment,name='finalizeaza_eveniment'),

]
