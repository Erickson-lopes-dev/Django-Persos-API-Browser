from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def register(request):
    # verifica se o método é get
    if request.method == 'GET':
        # retorna o template
        return render(request, 'registration/register.html')

    if request.method == 'POST':
        try:
            # tenta pegar os dados enviados do formulário
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            User.objects.create_user(
                username=username,
                password=password,
                email=email)
        except:
            return render(request, 'registration/register.html', {'message': f'Credenciais inválidas'})
        else:
            return redirect('/acconts/login/')
