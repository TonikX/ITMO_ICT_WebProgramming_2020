from django.http import HttpResponse
import datetime

def geeks_view(request):
    now = datetime.datetime.now()
    html = "Time is {}".format(now)

    return HttpResponse(html)