from django.shortcuts import render, redirect
from .models import Usuario

def inicio(request):
    return render(request, 'index.html')

def login(request):

    if request.method == 'POST':

        usuario = request.POST.get('usuario')
        password = request.POST.get('password')

        try:
            usuario_db = Usuario.objects.get(
                usuario=usuario,
                password=password
            )

            request.session['usuario'] = usuario_db.usuario

            return redirect('inicio')

        except Usuario.DoesNotExist:

            return render(request, 'login.html', {
                'error': 'Usuario o contraseña incorrectos'
            })

    return render(request, 'login.html')

def registro(request):

    if request.method == 'POST':

        usuario = request.POST.get('usuario')
        edad = request.POST.get('edad')
        password = request.POST.get('password')
        opinion = request.POST.get('opinion')

        # Verificar que no exista el usuario
        if not Usuario.objects.filter(usuario=usuario).exists():

            Usuario.objects.create(
                usuario=usuario,
                edad=edad,
                password=password,
                opinion=opinion
            )

        return redirect('inicio')

    return render(request, 'registro.html')

def noticias(request):
    return render(request, 'noticias.html')

def panel(request):
    return render(request, 'panel.html')

def desarrolladores(request):
    return render(request, 'desarrolladores.html')

def sistema(request):
    return render(request, 'sistema.html')