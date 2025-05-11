from django.shortcuts import render, redirect
from .forms import FormularioCadastro

def cadastro_views(request):
    if request.method == 'POST':
        form = FormularioCadastro(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # ou outra página após o cadastro
    else:
        form = FormularioCadastro()
    return render(request, 'cadastro/cadastro.html', {'form': form})

# Create your views here.
