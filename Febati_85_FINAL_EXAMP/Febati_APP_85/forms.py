from django import forms
from .models import Comentar,Producto

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentar
        fields = ['comentario']
        widgets = {
            'comentario': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['titulo', 'descripcion', 'imagen', 'precio']
        widgets = {
            'descripcion': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }