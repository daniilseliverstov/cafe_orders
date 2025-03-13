from django.shortcuts import render
from django.http import JsonResponse
from .models import Order
from .serializers import OrderSerializer
from rest_framework import generics


# Представление для отображения списка заказов (фронтенд)
def order_list_view(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})


# Представление для создания и получения списка заказов (REST API)
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# Представление для получения, обновления и удаления конкретного заказа (REST API)
class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
