from django.contrib import admin  # type: ignore

# Register your models here.
from .models import Car, Owner, Own, DriversLicense

admin.site.register([Car, Owner, Own, DriversLicense])
