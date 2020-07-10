from project_first_app.models import Owner, Car
from django.views import View
from .forms import OwnerForm
from django.views.generic.edit import CreateView


def NewOwnerForm(request):
    form = OwnerForm(request.POST)
    context = {}
    context["form"] = form

    if form.is_valid():
        form.save()

    return render(request, 'ownerform.html', context)


class NewCarForm(CreateView):
    model = Car
    fields = [
        "make",
        "model",
        "color",
        "gos_num"
    ]
    template_name = "carform.html"