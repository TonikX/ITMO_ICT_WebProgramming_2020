from django.template.backends import django
from django.shortcuts import render, redirect


def main_board(request):
    return render(request, 'main_page.html')


def redirect_main(request):
    return redirect('main_boar_url', permanent=True)

