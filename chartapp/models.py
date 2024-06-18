from django.db import models

# Create your models here.


class Fruits(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()

    class Meta:
        verbose_name = "Fruit"

    def __str__(self):
        return self.name