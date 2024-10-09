from django.urls import path
from .views import pedidos_list, pedidos_detail, pedidos_create, pedidos_item_create

urlpatterns = [
    path('', pedidos_list, name='pedidos_list'),  # Lista de pedidos
    path('pedidos_detail/<int:pedidos_id>/', pedidos_detail, name='pedidos_detail'),  # Detalhe de um pedido
    path('pedidos/create/', pedidos_create, name='pedidos_create'),  # Criar um novo pedido
    path('pedidos/<int:pedidos_id>/item/create/', pedidos_item_create, name='pedidos_item_create'),  # Criar um item do pedido
]
