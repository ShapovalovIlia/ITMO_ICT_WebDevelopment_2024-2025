from django.http import Http404
from django.shortcuts import render

from .models import AutoOwner


def auto_owner_info(request, poll_id):
    try:
        owner_data = AutoOwner.objects.get(
            pk=poll_id
        )

    except AutoOwner.DoesNotExist:
        raise Http404("AutoOwner does not exist")

    return render(
        request, "owner.html", {'owner': owner_data}
    )
