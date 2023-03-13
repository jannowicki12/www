from django.shortcuts import render
from django import forms
from .models import Item
class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

from django.http import HttpResponse
from django.shortcuts import render

def item_create(request):
    if request.method == "POST":
        form = ItemCreateForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = ItemCreateForm()
    return render(request, 'items/item_create.html', {'form': form})


def items_table(request):
    items = Item.objects.all()
    return render(request, 'items/items_table.html', {'items': items})

from django.http import JsonResponse
from django.shortcuts import render

from .models import Item


def items_table(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }

    return render(request, 'items/items_table.html', context=context)


def add_to_cart(request, item_id):
    # print('item id', item_id)
    cart_in_session = request.session['cart'] if 'cart' in request.session else []
    cart_in_session.append(item_id)
    request.session.update({'cart': cart_in_session})
    print('session', request.session['cart'])
    return JsonResponse({'message': 'Added item to cart.'})

def cart(request):
    context = {}
    cart = {}
    summary = 0
    print(request.session['cart'])
    if 'cart' in request.session:
        for item_id in request.session['cart']:
            price = Item.objects.get(id=item_id).price
            cart[item_id] =[
                Item.objects.get(id=item_id), 
                request.session['cart'].count(item_id),
                int(price) * request.session['cart'].count(item_id)
            ]
            summary += int(price) 
    if "clear-cart" in request.POST:
        request.session['cart'] = []
        print('clearing cart')
    context['items'] = cart
    context['summary'] = summary
    return render(request, 'items/cart.html', context=context)