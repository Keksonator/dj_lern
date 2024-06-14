from django.urls import path, register_converter
from blog import views, converters


register_converter(converters.FourDigitYearConverter, 'year4')


urlpatterns = [
    path('', views.index, name='home'),
    path('post/', views.posts, name='posts'),
    path('post/<int:post_id>', views.post_num, name='post_id'),
    path('post/<slug:post_slug>', views.post_slug, name='post_slug'),
    path("archive/<year4:year>/", views.archive, name='archive'),
]

