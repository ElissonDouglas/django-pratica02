from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Produto
from .forms import ProdutoModelForm

# Create your views here.
def index(request):
    produtos = Produto.objects.all()
    
    context = {
        'produtos': produtos,
    }
    return render(request, 'index.html', context)


def produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':  
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                prod=form.save()
                messages.success(request, 'Produto salvo com sucesso!')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Algo de errado aconteceu :(')
        else:
            form = ProdutoModelForm()
        context = {
            'form': form,
        }
        return render(request, 'produto.html', context)
    return redirect('index')

def prod(request, pk):
    prod = get_object_or_404(Produto, id=pk)
    context = {
        'produto': prod,
    }
    
    return render(request, 'prod.html', context)

def error404(request, exception):
    return render(request, '404.html')
