# Файл-маршрутизатор.

from django.urls import path
from . import views


# Если пользовательский запрос попадает в список urlpatterns, будет вызвана функция,
# которую можно найти в файле coolapp/views.py
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),  # для создания нового фильма
    path('films', views.films, name='films'),  # для отображения фильмов
    path('<int:film_id>/', views.new, name='new'),  # для вытаскивания из URN числа
]
