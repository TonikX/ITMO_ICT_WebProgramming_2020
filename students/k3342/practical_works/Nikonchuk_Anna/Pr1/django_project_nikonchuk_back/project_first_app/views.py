import django.shortcuts

from .models import Author


# Create your views here.
def authors_list(request):
    # print(request)
    # return HttpResponse('<h1>Hello!</h1>')
    authors = Author.objects.all()
    return django.shortcuts.render(request, 'project_first_app/index.html', context={'authors': authors})


def author_detail(request, slug):
    author = Author.objects.get(slug__iexact=slug)
    return django.shortcuts.render(request, 'project_first_app/author_detail.html', context={'author': author})
