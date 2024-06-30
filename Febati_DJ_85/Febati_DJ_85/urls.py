from django.contrib import admin
from django.urls import path
from Febati_APP_85 import views

urlpatterns = [
    path('', views.Vista_E_LN_85, name = 'el_mister'),
    path('RO/', views.Vista_E_RO_85, name='vista_ro'),
    path('LN/', views.Vista_E_LN_85, name='vista_ln'),
    path('SE/', views.Vista_E_SE_85, name='vista_se'),
    path('CS/', views.Vista_E_CS_85, name='vista_cs'),

]
