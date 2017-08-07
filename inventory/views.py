from django.shortcuts import render
from django.views import generic
from .models import Item


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'inventory/index.html'

    def get_queryset(self):
        return Item.objects.all()