from django.contrib import admin
from django.urls import path
from Febati_APP_85 import views

urlpatterns = [
    path('', views.Vista_E_PL_85, name = 'el_mister'),
    path('admin/', admin.site.urls),
    path('inicio/',views.Vista_E_PL_85, name = 'INICIO'),
    path('ayuda/',views.Vista_E_AA_85, name = 'AYUDA'),

    path('user/',views.Vista_E_UR_85, name = 'USER'),
    path('user/',views.Vista_E_CO_85, name = 'CARRITO')

]