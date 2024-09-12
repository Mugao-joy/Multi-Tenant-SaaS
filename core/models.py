from django.db import models

# Create your models here.
#tenant model
class Tenant(models.Model):
    HOUSE_SIZE_CHOICES = (
        ('1', '1 Bedroom'),
        ('2', '2 Bedrooms'),
        ('3', '3 Bedrooms'),
    )

    name = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)
    house_size = models.CharField(max_length=1, choices=HOUSE_SIZE_CHOICES)
    move_in_date = models.DateField(null =True, blank = True)

    def __str__(self):
        return f"{self.name} - House {self.house_number}"
