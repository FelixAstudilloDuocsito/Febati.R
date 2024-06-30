from django.shortcuts import render

# Create your views here.

def Vista_E_RO_85(request):
  return render(request, 'Estructura_RO_85.html', context={})

def Vista_E_LN_85(request):
  return render(request, 'Estructura_LN_85.html', context={})

def Vista_E_SE_85(request):
  return render(request, 'Estructura_SE_85.html', context={})

def Vista_E_CS_85(request):
  return render(request, 'Estructura_CS_85.html', context={})

