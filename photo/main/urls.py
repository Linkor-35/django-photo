from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('servises', views.servises, name='servises'),
    path('goods', views.goods, name='goods'),
    path('reklamma', views.reklamma, name='reklamma'),
    path('souvenirs', views.souvenirs, name='souvenirs'),
    path('workshop', views.workshop, name='workshop'),
    path('contacts', views.contacts, name='contacts'),
    path('upload/', views.upload, name='upload')
]
