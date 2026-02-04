from django.db import models


class Device(models.Model):
    STATUS_CHOICES = (
        ('AVAILABLE', 'Available for purchase'),
        ('SOLD', 'Sold'),
        ('RESTOCKING', 'Restocking soon'),
    )

    type = models.CharField(max_length=100, blank=False)
    price = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="SOLD")
    issues = models.CharField(max_length=20, default="None")


    class Meta:
        abstract = True

    def __str__(self):
        return f"Type: { self.type }, Price: { self.price }"
    

class Laptop(Device):
    pass
class Desktop(Device):
    pass
class Mobile(Device):
    pass