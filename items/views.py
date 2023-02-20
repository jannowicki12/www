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