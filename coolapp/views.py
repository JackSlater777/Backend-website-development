from django.shortcuts import render
from django.shortcuts import redirect
from .models import Film
from .forms import FilmForm


def index(request):
    """
    Некая функция index, которая принимает запрос и отправляет HTTP-ответ
    """
    return render(request, 'coolapp/index.html')


def films(request):
    """
    Запрос пользователя прилетает в фукнцию films;
    Контроллер берет шаблон films.html, фильмы из базы данных, оформляем фильмы
    в виде словаря: по ключу из словаря проходимся в языке шаблонов (films.html);
    И шаблон, и данные передаются в функцию render;
    Render делает подстановки и возвращает результаты пользователю
    """
    return render(request, 'coolapp/films.html', {'films': Film.objects.all()})


def new(request, film_id=None):
    """
    Пользователь набрал домен/new - запрос прилетел сюда - метод GET - else
    Пользователь заполнил форму и нажал Save - метод POST - создается новая форма, в неё передается request.POST
    Происходит переадресация на страницу домен/film_id
    """
    if request.method == "POST":
        form = FilmForm(request.POST)
        if form.is_valid():
            film = form.save()
            return redirect('/{}'.format(film.id), film=film)
    if film_id:
        film = Film.objects.get(id=film_id)
    else:
        film = Film()
    return render(request, 'coolapp/new.html',
                  {'form': FilmForm(instance=film)})
