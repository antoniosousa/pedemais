from django import forms
from .models import Pedidos, PedidosItem

class PedidosForm(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = ['status', 'total_preco']  # Adicione outros campos se necessário

class PedidosItemForm(forms.ModelForm):
    class Meta:
        model = PedidosItem
        fields = ['preco', 'quantidade']  # Adicione outros campos se necessário
