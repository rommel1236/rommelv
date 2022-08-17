from django.shortcuts import render

# Create your views here.
def holamundoCore(request):
    return render(request,'core.html')

def noticias(request):
    return render(request, 'noticias.html')

def farandula(request):
    return render(request, 'farandula.html')

def deportes(request):
    return render(request, 'deportes.html')

#############################################################

def ini(request):
    return render(request,'herencias/inicio.html')

def quienesomos(request):
    return render(request, 'herencias/quienesomos.html')

def producto(request):
    return render(request, 'herencias/producto.html')

def contacto(request):
    return render(request, 'herencias/contacto.html')

def quienes(request):
    return render(request, 'herencias/quienessomos.html')