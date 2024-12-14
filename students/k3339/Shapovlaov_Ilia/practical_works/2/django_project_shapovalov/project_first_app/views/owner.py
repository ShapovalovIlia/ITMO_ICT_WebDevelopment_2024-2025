from django.http import Http404, HttpRequest, HttpResponse  # type: ignore
from django.shortcuts import render  # type: ignore

from project_first_app.models import Owner
from project_first_app.forms import OwnerForm


def owner(request: HttpRequest, owner_id: int) -> HttpResponse:
    try:
        owner_data = Owner.objects.get(pk=owner_id)

    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, "owner/get.html", {"owner": owner_data})


def owner_list(request: HttpRequest) -> HttpResponse:
    context = {}
    context["owners"] = Owner.objects.all()

    return render(request, "owner/list.html", context)


def owner_create(request: HttpRequest) -> HttpResponse:
    context = {}
    form = OwnerForm(request.POST or None)

    if form.is_valid():
        form.save()
    context["form"] = form
    return render(request, "owner/create.html", context)
