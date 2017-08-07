from django.shortcuts import render
from django.views import generic
from .models import Item, Loaner 


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'inventory/index.html'
    context_object_name = 'items' # use to access list of items in index.html

    def get_queryset(self):
        return Item.objects.all()