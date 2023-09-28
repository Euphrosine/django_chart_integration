from django.db import models

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    types = models.CharField(max_length=100, null=False, blank=False)
    qty_of_products = models.IntegerField()

    def __str__(self):
        return f'{self.types} - {self.qty_of_products}'
