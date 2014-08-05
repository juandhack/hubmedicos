from django.conf.urls import patterns, include, url
from .views import Perfil,Tarjeta

urlpatterns = patterns('',

	url(r'^home/$' , Perfil.as_view(), name='perfil'),
    #url(r'^tarjeta/$' ,Tarjeta.as_view(), name='tarjeta'),

)