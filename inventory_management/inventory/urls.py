from django.urls import path
from .views import inventory_create , inventory_stock , inventory_delete

urlpatterns = [
    path('inventory/', inventory_create, name='inventory-create'),
    path('inventory/stock/', inventory_stock, name='inventory-stock'),
    path('inventory/delete/<int:item_id>/', inventory_delete, name='inventory-delete'),

]
