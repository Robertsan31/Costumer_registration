# clientes/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

def home(request):
    query = request.GET.get('q')
    if query:
        # Ordenar os resultados para garantir uma paginação consistente
        clientes_list = Cliente.objects.filter(
            Q(nome__icontains=query) | Q(email__icontains=query)
        ).order_by('nome')
    else:
        # Ordenar os resultados para garantir uma paginação consistente
        clientes_list = Cliente.objects.all().order_by('nome')

    # Configuração da paginação
    paginator = Paginator(clientes_list, 5) # Mostrar 5 clientes por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj, # Passar o objeto da página para o template
        'query': query,
    }
    return render(request, 'clientes/home.html', context)

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('clientes:home_clientes')
    else:
        form = ClienteForm()

    context = {
        'form': form,
        'titulo_pagina': 'Cadastrar Novo Cliente'
    }
    return render(request, 'clientes/cadastro.html', context)

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect('clientes:home_clientes')
    else:
        form = ClienteForm(instance=cliente)

    context = {
        'form': form,
        'titulo_pagina': 'Editar Cliente',
        'cliente': cliente
    }
    return render(request, 'clientes/editar_cliente.html', context)

def excluir_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        nome_cliente = cliente.nome
        cliente.delete()
        messages.success(request, f'Cliente "{nome_cliente}" excluído com sucesso!')
        return redirect('clientes:home_clientes')
    
    context = {
        'cliente': cliente
    }
    return render(request, 'clientes/excluir_cliente_confirm.html', context)
