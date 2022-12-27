from django.urls import path
from stock.views import stock_list, stock_detail, stock_sale_detail, stock_buy, stock_sale, account


urlpatterns = [
    path('list/', stock_list, name='list'),
    path('detail/<int:pk>/', stock_detail, name='detail'),
    path('detail_sale/<int:pk>/', stock_sale_detail, name='sale_detail'),
    path('buy/<int:pk>/', stock_buy, name='buy'),
    path('sale/<int:pk>/', stock_sale, name='sale'),
    path('account/', account, name='account')
]