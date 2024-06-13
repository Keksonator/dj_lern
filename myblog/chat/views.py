from django.shortcuts import render
from django.http import HttpResponse


def all_chat(request):
    return HttpResponse("Список чатов")


def сhat(request):
    return HttpResponse("Чат с определённым пользователем")
