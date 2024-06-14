import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'ЧН', 'Черновик'
        PUBLISHED = 'ОП', 'Опубликован'

    title = models.CharField('Заголовок', max_length=150)
    slug = models.SlugField('slug',max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    text = models.TextField('Текст')
    publish = models.DateTimeField('Опубликован', default=timezone.now)
    created = models.DateTimeField('Создан', auto_now_add=True)
    update = models.DateTimeField('Обновлён', auto_now=True)
    status = models.CharField('', max_length=2,
                              choices=Status.choices, default=Status.DRAFT)
