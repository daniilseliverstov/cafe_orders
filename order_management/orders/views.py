from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from .forms import OrderForm
from .models import Order
from .serializers import OrderSerializer
from rest_framework import generics


def order_list_view(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


def add_order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.status = 'pending'
            order.save()
            return redirect('orders:order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/add_order.html', {'form': form})


def delete_order_view(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('orders:order_list')
    return render(request, 'orders/delete_order.html', {'order': order})


def search_order_view(request):
    query = request.GET.get('query', '')
    status = request.GET.get('status', '')
    if query.isdigit():
        orders = Order.objects.filter(table_number=int(query))
    else:
        orders = Order.objects.filter(items__contains=query)
    if status:
        orders = orders.filter(status=status)
    return render(request, 'orders/order_list.html', {'orders': orders, 'query': query, 'status': status})


def revenue_view(request):
    total_revenue = Order.objects.filter(status='paid').aggregate(total=Sum('total_price'))['total'] or 0
    return render(request, 'orders/revenue.html', {'total_revenue': total_revenue})
