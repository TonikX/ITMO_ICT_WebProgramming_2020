from django.template.backends import django
from django.shortcuts import render


def main_board(request):
    return render(request, 'main_page.html')



