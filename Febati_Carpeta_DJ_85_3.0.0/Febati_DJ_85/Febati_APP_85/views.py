from django.shortcuts import render

# Create your views here.

def Vista_E_PL_85(request):
  return render(request, 'Estructura_PL_85.html', context={})

def Vista_E_AA_85(request):
  return render(request, 'Estructura_AA_85.html', context={})

def Vista_E_UR_85(request):
  return render(request, 'Estructura_UR_85.html', context={})



