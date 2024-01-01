from django.http import HttpResponse
from .models import InventoryItem
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

def inventory_delete(request, item_id):
    if request.method == 'POST':
        InventoryItem.objects.filter(id=item_id).delete()
    return redirect('inventory-stock')

@csrf_exempt
def inventory_create(request):
    if request.method == 'POST':
        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        
        # Check if item already exists in the inventory
        if InventoryItem.objects.filter(item=item).exists():
            # Item already exists, update the quantity
            inventory_item = InventoryItem.objects.get(item=item)
            inventory_item.quantity = quantity
            inventory_item.save()
        else:
            # Item does not exist, create a new inventory item
            InventoryItem.objects.create(item=item, quantity=quantity)
        
        return HttpResponse(status=201)
    else:
        return HttpResponse(status=405)


def inventory_stock(request):
    inventory = InventoryItem.objects.all() 
    is_empty = False
    
    if not inventory:
        is_empty =True
        
    return render(request, 'inventory/inventory_stock.html', {'inventory': inventory, 'is_empty': is_empty})


