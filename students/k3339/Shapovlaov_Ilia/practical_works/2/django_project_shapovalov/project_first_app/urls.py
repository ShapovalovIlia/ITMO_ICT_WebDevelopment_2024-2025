from django.urls import path  # type: ignore

from project_first_app.views import (
    owner,
    owner_list,
    owner_create,
    CarUpdateView,
    CarDetailView,
    CarListView,
    CarCreateView
)

urlpatterns = [
    path(
        "owner/<int:owner_id>/",
        owner,
        name="owner",
    ),
    path("owner/list", owner_list, name="owner_list"),
    path("owner/create", owner_create, name="owner_create"),
    path("car/list", CarListView.as_view(), name="car_list"),
    path("car/<int:pk>/", CarDetailView.as_view(), name="car"),
    path("car/<int:pk>/update", CarUpdateView.as_view(), name="car_update"),
    path("car/create", CarCreateView.as_view(), name="car_create")
]
