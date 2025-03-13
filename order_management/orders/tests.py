from django.test import TestCase
from .models import Order


class OrderModelTest(TestCase):
    def test_create_order(self):
        order = Order.objects.create(
            table_number=5,
            items=['Pizza', 'Coke'],
            total_price=15.99,
            status='pending'
        )
        self.assertEqual(order.table_number, 5)
        self.assertEqual(order.status, 'pending')
