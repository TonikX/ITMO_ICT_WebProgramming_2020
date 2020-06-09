from django import forms
# from project_first_app.models import CarOwner


"""
    class OwnerForm(forms.ModelForm):

    class Meta:
        model = CarOwner

        fields = [
            "first_name",
            "last_name",
            "birth_date"
        ]
"""


""" Это надо вставить во views.py
def create_view(request):
    context = {}

    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)
"""
