from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns=[
    path('home/', views.home, name='home'),
    path('quiensoy', views.quiensoy, name='quiensoy'),
    path('criptos', views.criptos, name='criptos'),
    path('criptos/agregar', views.create, name='create'),
    path('criptos/editar', views.update, name='update'), 
    path('criptos/<int:id>', views.getById, name='getById'),
    path('eliminar/<int:id>', views.delete, name='delete'), 
    path('criptos/editar/<int:id>', views.update, name='update'),
    path('criptos/excelResult', views.excelResult, name='excelResult'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)