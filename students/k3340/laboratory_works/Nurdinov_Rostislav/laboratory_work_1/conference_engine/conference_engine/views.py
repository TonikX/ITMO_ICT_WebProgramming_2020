from django.http import HttpResponse


def conference(request):
    return HttpResponse('<h1>HEllo</h1>')

