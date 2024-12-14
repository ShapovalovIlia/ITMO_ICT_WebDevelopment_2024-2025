from django.views.generic import ListView, DetailView, UpdateView, CreateView  # type: ignore
from django.urls import reverse_lazy  # type: ignore

from project_first_app.models import Car
from project_first_app.forms import CarForm


class CarListView(ListView):
    model = Car
    template_name = "car/list.html"
    context_object_name = "cars"


class CarDetailView(DetailView):
    model = Car
    template_name = "car/get.html"
    context_object_name = "car"


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = "car/update.html"
    success_url = reverse_lazy("car_list")


class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = "car/create.html"
    success_url = reverse_lazy("car_list")
