from django.http import HttpResponse
from django.shortcuts import redirect

def redirect_hw(request):
    return redirect('hw_list_url', permanent=True)