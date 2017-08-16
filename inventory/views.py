from django.shortcuts import render
from django.views import generic
from .models import Item, Loaner 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .python import services 

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'inventory/index.html'
    context_object_name = 'items' # use to access list of items in index.html

    def get_queryset(self):
        return Item.objects.all()


class InStock(generic.ListView):
    template_name = 'inventory/in_stock.html'
    context_object_name = 'items' 

    def get_queryset(self):
        return Item.objects.filter(checked_out = False)


class OutofStock(generic.ListView):
    template_name = 'inventory/checked_out.html'
    context_object_name = 'items' 

    def get_queryset(self):
        return Item.objects.filter(checked_out = True)

class DetailView(generic.DetailView):
    model = Item
    template_name = 'inventory/detail.html'

class ItemCreate(CreateView): 
	model = Item 
	fields = ['make_and_model', 'label', 'notes', 'checked_out']

class ItemUpdate(UpdateView):
    model = Item
    fields = ['make_and_model', 'label', 'notes', 'checked_out']
    template_name_suffix = '_update_form'


class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('inventory:index') #redirect to here after delete

class LoanerCreate(CreateView): 
	model = Loaner 
	fields = ['item','net_id']


def loaner_detail(request, netid): 
    name = services.display_name(netid)
    return render(request, 'inventory/user_detail.html', {'result': name})
