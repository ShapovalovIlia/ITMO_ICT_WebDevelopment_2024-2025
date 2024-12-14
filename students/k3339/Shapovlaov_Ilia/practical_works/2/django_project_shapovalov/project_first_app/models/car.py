from django.db import models  # type: ignore


class Car(models.Model):
    state_number = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    colour = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.state_number} {self.brand} {self.model} {self.colour}"
