from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_list_view, name='order_list'),
    path('api/orders/', views.OrderListCreateView.as_view(), name='order-list-create'),
    path('api/orders/<int:pk>/', views.OrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),
]