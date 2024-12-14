from django.db import models  # type: ignore


class Owner(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.name} {self.surname} {self.date_of_birth}"
