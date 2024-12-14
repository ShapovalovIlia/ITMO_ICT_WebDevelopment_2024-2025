__all__ = [
    "owner",
    "owner_list",
    "owner_create",
    "CarDetailView",
    "CarListView",
    "CarUpdateView",
    "CarCreateView",
]

from .owner import owner, owner_list, owner_create
from .car import CarDetailView, CarListView, CarUpdateView, CarCreateView
