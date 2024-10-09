from django.shortcuts import render, get_object_or_404, redirect
from .models import Pedidos, PedidosItem  # noqa: F401
from .forms import PedidosItemForm, PedidosForm  # Crie os formulários correspondentes

def pedidos_list(request):
    pedidos = Pedidos.objects.all()  # noqa: F821
    return render(request, 'pedidos_list.html', {'pedidos': pedidos})

def pedidos_detail(request, pedidos_id):
    pedidos = get_object_or_404(Pedidos, id=pedidos_id)
    return render(request, 'pedidos_detail.html', {'pedidos': pedidos})

def pedidos_create(request):
    if request.method == 'POST':
        form = PedidosForm(request.POST)  # noqa: F821
        if form.is_valid():
            pedidos = form.save()
            return redirect('pedidos_detail', pedidos_id=pedidos.id)
    else:
        form = PedidosForm()  # noqa: F821
    return render(request, 'pedidos_form.html', {'form': form})

def pedidos_item_create(request, order_id):
    pedidos = get_object_or_404(Pedidos, id=pedidos),  # noqa: F821
    if request.method == 'POST':
        form = PedidosItemForm(request.POST)
        if form.is_valid():
            pedidos_item = form.save(commit=False)
            pedidos_item.pedidos = pedidos  # noqa: F821
            pedidos_item.save()
            return redirect('pedidos_detail', pedidos_id=pedidos.id)
    else:
        form = PedidosItemForm()
    return render(request, 'pedidos_item_form.html', {'form': form, 'pedidos': pedidos})
