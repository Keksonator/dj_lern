from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse('Helloy')


def posts(request,):
    return HttpResponse("<h1>Список постов</h1>")


def post_num(request, post_id):
    return HttpResponse(f"<h1>Пост #{post_id}</h1>")


def post_slug(request, post_slug):
    return HttpResponse(f"<h1>Пост #{post_slug}</h1>")


def archive(request, year):
    return HttpResponse(f"<h1>Архив по году {year}</h1>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
