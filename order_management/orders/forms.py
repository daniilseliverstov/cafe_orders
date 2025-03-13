from django import forms
from .models import Order, Dish


class OrderForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(
        queryset=Dish.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Вы можете использовать другие виджеты, например, Select
        required=True
    )

    class Meta:
        model = Order
        fields = ['table_number', 'items', 'status']