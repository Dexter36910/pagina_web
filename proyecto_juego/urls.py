from django.contrib import admin
from django.urls import path
from usuarios.views import (
    inicio,
    login,
    registro,
    noticias,
    panel,
    desarrolladores,
    sistema
)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('noticias/', noticias, name='noticias'),
    path('panel/', panel, name='panel'),
    path('desarrolladores/', desarrolladores, name='desarrolladores'),
    path('sistema/', sistema, name='sistema'),
    path('admin/', admin.site.urls),
]