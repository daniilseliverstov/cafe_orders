from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    # Фронтенд маршруты
    path('', views.order_list_view, name='order_list'),
    path('add/', views.add_order_view, name='add_order'),
    path('delete/<int:pk>/', views.delete_order_view, name='delete_order'),
    path('revenue/', views.revenue_view, name='revenue'),
    path('search/', views.search_order_view, name='search_order'),

    # API маршруты
    path('api/orders/', views.OrderListCreateView.as_view(), name='api_order_list_create'),
    path('api/orders/<int:pk>/', views.OrderRetrieveUpdateDestroyView.as_view(), name='api_order_detail'),
]
