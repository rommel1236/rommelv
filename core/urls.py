from django.urls import path
from . import views
urlpatterns = [
    path('', views.holamundoCore,name='core'),
    path('noticias',views.noticias,name='noticias'),
    path('deportes',views.deportes,name='deportes'),
    path('farandula',views.farandula,name='farandula'),
    path('inicio', views.ini,name='inicio'),
    path('quienesomos',views.quienesomos,name='quienesomos'),
    path('producto',views.producto,name='producto'),
    path('contacto',views.contacto,name='contacto'),
    path('quienessomos',views.quienes,name='quienessomos'),
]