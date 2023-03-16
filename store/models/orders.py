from email.headerregistry import Address
from django.db import models
from .product import Product
from .customer import Customer
import django

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default="", blank=True)
    mob_number = models.IntegerField(blank=False)
    date = models.DateTimeField(default=django.utils.timezone.now())
    status = models.BooleanField(default=False)

    def place_order(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id)