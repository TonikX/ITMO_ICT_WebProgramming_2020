from django.http import Http404, HttpResponse
from django.shortcuts import render
from project_first_app.models import Owner

def detail(request, owner_id):
    try:
        o = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, "Owner.html", {'owner': o})
    #return HttpResponse("<html><body>Имя: '{{ o.first_name }}', Фамилия: '{{ o.last_name }}' </body></html>")

def post_list(request):
    return HttpResponse('<h1>Hello!</h1>')

