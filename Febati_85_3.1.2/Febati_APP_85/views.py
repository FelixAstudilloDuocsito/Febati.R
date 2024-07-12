from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from django.views import View
from django.db import IntegrityError


def Vista_E_RO_85(request):
    return render(request, 'Estructura_RO_85.html', context={})

def Vista_E_LN_85(request):
    return render(request, 'Estructura_LN_85.html', context={})

def Vista_E_SE_85(request):
    return render(request, 'Estructura_SE_85.html', context={})

def Vista_E_CS_85(request):
    return render(request, 'Estructura_CS_85.html', context={})

def Vista_E_PL_85(request):
  return render(request, 'Estructura_PL_85.html')


def Vista_E_AA_85(request):
  return render(request, 'Estructura_AA_85.html')


def Vista_E_UR_85(request):
  return render(request, 'Estructura_UR_85.html')

def Vista_E_CO_85(request):
  return render(request, 'Estructura_CO_85.html')

def prueba(request):
    usuarios = Usuario.objects.all()
    context = {"usuarios": usuarios}
    return render(request, 'prueba.html', context)

class RegView(View):

    def get(self, request):
        return render(request, "Estructura_RO_85.html")

    def post(self, request):
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        usuario = request.POST.get('usuario')
        contrasena = request.POST.get('contrasena')
        confirmar_contrasena = request.POST.get('confirmar_contrasena')

        # Validación 
        if not all([nombre, correo, usuario, contrasena, confirmar_contrasena]):
            return render(request, "Estructura_RO_85.html", {"mensaje": "Todos los campos son obligatorios."})

        if contrasena != confirmar_contrasena:
            return render(request, "Estructura_RO_85.html", {"mensaje": "Las contraseñas no coinciden."})

      
        if Usuario.objects.filter(correo=correo).exists():
            return render(request, "Estructura_RO_85.html", {"mensaje": "El correo electrónico ya está registrado."})

        try:
            # Guardar usuario
            Usuario.objects.create(
                nombre=nombre,
                correo=correo,
                usuario=usuario,
                contraseña=contrasena
            )
            return render(request, "Estructura_RO_85.html", {"mensaje": "Registro exitoso"})
        except IntegrityError as e:
            return render(request, "Estructura_RO_85.html", {"mensaje": f"Error al registrar usuario: {str(e)}"})


class LoginView(View):

    def get(self, request):
        return render(request, "Estructura_LN_85.html")

    def post(self, request):
        usuario = request.POST.get('usuario')
        contraseña = request.POST.get('contrasena')

        # Verificar 
        try:
            user = Usuario.objects.get(usuario=usuario, contraseña=contraseña)
            if user:
               
                return redirect('INICIO')  
            else:
                return render(request, "Estructura_LN_85.html", {"mensaje": "Usuario o contraseña incorrectos."})
        except Usuario.DoesNotExist:
            return render(request, "Estructura_LN_85.html", {"mensaje": "Usuario o contraseña incorrectos."})


class EditUserView(View):

    def get(self, request, pk):
        usuario = get_object_or_404(Usuario, pk=pk)
        return render(request, "editar_usuario.html", {"usuario": usuario})

    def post(self, request, pk):
        usuario = get_object_or_404(Usuario, pk=pk)
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        usuario_nombre = request.POST.get('usuario')
        contrasena = request.POST.get('contrasena')
        confirmar_contrasena = request.POST.get('confirmar_contrasena')

        # Validación 
        if not all([nombre, correo, usuario_nombre, contrasena, confirmar_contrasena]):
            return render(request, "editar_usuario.html", {"mensaje": "Todos los campos son obligatorios.", "usuario": usuario})

        if contrasena != confirmar_contrasena:
            return render(request, "editar_usuario.html", {"mensaje": "Las contraseñas no coinciden.", "usuario": usuario})

        
        if Usuario.objects.filter(correo=correo).exclude(pk=pk).exists():
            return render(request, "editar_usuario.html", {"mensaje": "El correo electrónico ya está registrado por otro usuario.", "usuario": usuario})

        try:
            # Actualizar usuario
            usuario.nombre = nombre
            usuario.correo = correo
            usuario.usuario = usuario_nombre
            usuario.contraseña = contrasena
            usuario.save()
            return redirect('vistaL')  
        except IntegrityError as e:
            return render(request, "editar_usuario.html", {"mensaje": f"Error al actualizar usuario: {str(e)}", "usuario": usuario})
        
class EliminarUsuarioView(View):
    def post(self, request, pk):
        usuario = get_object_or_404(Usuario, pk=pk)
        usuario.delete()
        return redirect('vistaL')