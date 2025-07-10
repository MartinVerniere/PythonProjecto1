from django.http import HttpResponse

def saludo(request):
    contexto = {'mensaje': 'Hola Django - Coder'}
    return render(request, 'miapp/saludo.html', contexto)