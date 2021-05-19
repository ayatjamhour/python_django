from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('destroy', views.reset),	
    path('destroy', views.destroy),
    path('count', views.add), 	   
]