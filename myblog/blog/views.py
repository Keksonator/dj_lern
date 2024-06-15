from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Post


def index(request):
    return render(request, 'blog/index.html',)


def about(request):
    data = {'title': 'О сайте'}
    return render(request,  'blog/about.html', data)


def posts(request,):
    all_post = Post.objects.all()
    return render(request, 'blog/posts.html', {"all_post" : all_post})


def post_num(request, post_id):
      post = get_object_or_404(Post, pk=post_id)
      return render(request, 'blog/one_post.html', {'post': post})


def post_slug(request, post_slug):
    return HttpResponse(f"<h1>Пост {post_slug}</h1>")


def archive(request, year):
    if year > 2024:
        uri = reverse('post_slug', args=('music', ))
        return HttpResponseRedirect(uri)
    return HttpResponse(f"<h1>Архив по году {year}</h1>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
