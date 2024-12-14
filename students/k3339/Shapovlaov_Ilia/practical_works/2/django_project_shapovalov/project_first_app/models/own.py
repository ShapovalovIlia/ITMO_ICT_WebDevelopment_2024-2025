from django.db import models  # type: ignore

from .owner import Owner
from .car import Car


class Own(models.Model):
    owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
    )
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.owner.surname} {self.car} {self.start_date} {self.end_date}"
