from django.contrib import admin
from django.urls import path
from Febati_APP_85 import views
from Febati_APP_85.views import RegView,EditUserView

urlpatterns = [
    path('', views.Vista_E_LN_85, name = 'el_mister'),
    path('RO/', views.Vista_E_RO_85, name='vista_ro'),
    path('LN/', views.Vista_E_LN_85, name='vista_ln'),
    path('SE/', views.Vista_E_SE_85, name='vista_se'),
    path('CS/', views.Vista_E_CS_85, name='vista_cs'),
    path('admin/', admin.site.urls),
    path('lista/', views.prueba, name='vistaL'),
    path('registro/', RegView.as_view(), name='registro'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('editar/<int:pk>/', EditUserView.as_view(), name='editar_usuario'),
    path('eliminar/<int:pk>/', views.EliminarUsuarioView.as_view(), name='eliminar_usuario'),
    path('inicio/',views.Vista_E_PL_85, name = 'INICIO'),
    path('ayuda/',views.Vista_E_AA_85, name = 'AYUDA'),
    path('user/',views.Vista_E_UR_85, name = 'USER'),
    path('carrito/',views.Vista_E_CO_85, name = 'CARRITO'),
]
