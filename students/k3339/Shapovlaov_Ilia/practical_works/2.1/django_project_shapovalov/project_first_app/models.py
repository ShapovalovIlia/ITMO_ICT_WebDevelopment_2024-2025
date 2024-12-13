from django.db import models  # type: ignore


# Create your models here.
class AutoOwner(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    date_of_birth = models.DateTimeField()

    def __str__(self):
        return f"{self.name} {self.surname} {self.date_of_birth}"


class Auto(models.Model):
    state_number = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    colour = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.state_number} {self.brand} {self.model} {self.colour}"


class Own(models.Model):
    owner_id = models.ForeignKey(
        AutoOwner,
        on_delete=models.CASCADE,
    )
    auto_id = models.ForeignKey(Auto, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.owner_id.surname} {self.auto_id} {self.start_date} {self.end_date}"


class DriversLicense(models.Model):
    owner_id = models.ForeignKey(AutoOwner, on_delete=models.CASCADE)
    nubmer = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_of_issue = models.DateTimeField()

    def __str__(self):
        return f"{self.owner_id.surname} {self.nubmer} {self.type} {self.date_of_issue}"
