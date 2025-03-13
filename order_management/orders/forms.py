from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    items = forms.JSONField(widget=forms.Textarea,
                            help_text="Enter items as JSON, e.g., [{'name': 'Pizza', 'price': 10.99}, {'name': "
                                      "'Coke', 'price': 2.99}]")

    class Meta:
        model = Order
        fields = ['table_number', 'items']