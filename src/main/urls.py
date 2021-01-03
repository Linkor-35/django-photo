from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('servises', views.servises, name='servises'),
    path('goods', views.goods, name='goods'),
    path('reklamma', views.reklamma, name='reklamma'),
    path('souvenirs', views.souvenirs, name='souvenirs'),
    path('workshop', views.workshop, name='workshop'),
    path('contacts', views.contacts, name='contacts'),
    path('upload/', views.upload, name='upload'),
    path('upload_done', views.upload, name='done')
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)