from django.contrib import admin
from django.urls import path
# El punto (.) le dice a Django que busque views.py en esta misma subcarpeta
from .views import vista_panel_sustentabilidad 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sustentabilidad/panel/', vista_panel_sustentabilidad, name='panel_sustentabilidad'),
]
