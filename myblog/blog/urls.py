from django.urls import path, re_path, register_converter
from blog import views, converters


register_converter(converters.FourDigitYearConverter, 'year4')


urlpatterns = [
    path('', views.index),
    path('posts/', views.posts),
    path('posts/post/<int:post_id>', views.post_num),
    path('posts/post/<slug:post_slug>', views.post_slug),
    path("archive/<year4:year>/", views.archive),
]

