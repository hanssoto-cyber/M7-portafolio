from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.listar_productos, name='listar_productos'),
]