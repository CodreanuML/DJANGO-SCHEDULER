from django.urls import include,path
from django.contrib.auth import views as auth_views
from . import views as ACCOUNTS_VIEWS

app_name="ACCOUNTS" 



urlpatterns=[
	path('signup/',ACCOUNTS_VIEWS.signup,name='signup'),
	
	path('login/',ACCOUNTS_VIEWS.login,name='login'),

	path('logout/',auth_views.LogoutView.as_view(),name='logout'),


]