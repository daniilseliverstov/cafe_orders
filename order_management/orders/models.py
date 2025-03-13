from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.price} руб."


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершен'),
        ('paid', 'Оплачен'),
    ]

    id = models.AutoField(primary_key=True)  # Уникальный ID
    table_number = models.IntegerField()
    items = models.ManyToManyField(Dish, related_name='orders')  # Связь с моделью Dish
    total_price = models.FloatField(editable=False)  # Общая стоимость, вычисляемая автоматически
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def save(self, *args, **kwargs):
        # Рассчитываем общую стоимость заказа
        self.total_price = sum(dish.price for dish in self.items.all())
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Заказ {self.id} - Стол {self.table_number}"

    def save(self, *args, **kwargs):
        self.total_price = sum(item['price'] for item in self.items)
        super().save(*args, **kwargs)
