from django.db import models  # type: ignore

from .owner import Owner


class DriversLicense(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    nubmer = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_of_issue = models.DateField()

    def __str__(self):
        return f"{self.owner.surname} {self.nubmer} {self.type} {self.date_of_issue}"
