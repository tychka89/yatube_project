from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse('Главная страница')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request, any_slug):
    return HttpResponse(f'Любой слизняк {any_slug}')
