from django.contrib import admin
from .models import Usuario, Comentar,Producto,Imagen_Producto
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Comentar)
admin.site.register(Producto)
admin.site.register(Imagen_Producto)