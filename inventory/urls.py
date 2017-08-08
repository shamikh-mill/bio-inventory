from django.conf.urls import url
from . import views

app_name = 'inventory'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'item/add/$', views.ItemCreate.as_view(), name = "item-add"),
    url(r'loaner/add/$', views.LoanerCreate.as_view(), name = "loaner-add"),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),
]