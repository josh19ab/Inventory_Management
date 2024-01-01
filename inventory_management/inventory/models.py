from django.db import models

class InventoryItem(models.Model):
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.item
