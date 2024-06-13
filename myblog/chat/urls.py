from django.urls import path
from chat import views

urlpatterns = [
    path('', views.all_chat),
    path('chat/<int:chat_id>', views.сhat),
]