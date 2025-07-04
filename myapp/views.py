from django.shortcuts import render

# Create your views here.
def index(request):
    contexto = {
        'mensaje': 'Hola Mundo'
    }
    return render(request, 'myapp/index.html', contexto)