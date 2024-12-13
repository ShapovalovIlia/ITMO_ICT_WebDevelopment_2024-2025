from django.contrib import admin

# Register your models here.
from .models import AutoOwner, Auto, Own, DriversLicense

admin.site.register([AutoOwner, Auto, Own, DriversLicense])
