from django.urls import path
from . import views

app_name = 'tracking'

urlpatterns = [
    path('', views.main),
    path('get_ip', views.getClientIp, name='get_ip'),
    path('track_all_info/', views.getUserAllDeliverInfo, name='track_all_info'),
    path('get_order/<int:id>', views.getUserOrder, name='get_order'),
    path('check_order_list', views.check_order_list, name='check_order_list'),
    path('add_order_price', views.addOrderPrice, name='add_order_price'),
]