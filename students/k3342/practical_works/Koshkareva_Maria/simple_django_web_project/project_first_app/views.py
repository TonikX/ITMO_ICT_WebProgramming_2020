from django.shortcuts import render
from django.http import Http404
from .models import Owner, Ownership, Driver_license


def Owner_list(request, owner_id):
    try:
        the_owner = Owner.objects.get(pk=owner_id)
        license = Driver_license.objects.get(driver=the_owner)
        owns = Ownership.objects.filter(owner=the_owner)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, "project_first_app/owner_list.html",
                                            {"owner":the_owner,
                                             "owns":owns,
                                             "license":license})
