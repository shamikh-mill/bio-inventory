from django.conf.urls import url
from . import views

app_name = 'inventory'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'stock/$', views.InStock.as_view(), name = 'in-stock'),
    url(r'checked-out/$', views.OutofStock.as_view(), name = 'checked-out'),
    url(r'item/add/$', views.ItemCreate.as_view(), name = "item-add"),
    url(r'loaner/add/$', views.LoanerCreate.as_view(), name = "loaner-add"),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),
    url(r'item/(?P<pk>[0-9]+)/delete/$', views.ItemDelete.as_view(), name = 'item-delete'),
    url(r'item/(?P<pk>[0-9]+)/$', views.ItemUpdate.as_view(), name = 'item-update'),
    url(r'^user/(?P<netid>[\w.@+-]+)/$',views.loaner_detail, name='laoner-detail'),
]