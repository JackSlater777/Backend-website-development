from django.shortcuts import render
from django.shortcuts import redirect
from .models import Film
from .forms import FilmForm


def index(request):
    """
    Некая функция index, которая принимает запрос и отправляет HTTP-ответ
    """
    # return render(request, 'coolapp/index.html')
    return render(request, 'coolapp/index.html', {'sitename': 'about films'})


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
    # Пользователь заполнил форму и нажал Save - метод POST - создается новая форма, в неё передается request.POST
    # Происходит переадресация на страницу домен/film_id
    if request.method == "POST":
        form = FilmForm(request.POST)
        if form.is_valid():
            # Если сохраняем данные про новый фильм
            if not film_id:
                film = form.save()  # Сохранение экземпляра фильма в базу данных (здесь происходит генерация films.id)
                return redirect(f'/coolapp/{film.id}', film=film)
            # Если обновляем данные уже внесенного фильма
            else:
                film = Film.objects.get(id=film_id)
                form = FilmForm(request.POST, instance=film)
                form.save()

    # Пользователь набрал домен/film_id - запрос прилетел сюда - метод GET
    if film_id:
        film = Film.objects.get(id=film_id)

    # Пользователь набрал домен/new - запрос прилетел сюда - метод GET
    else:
        film = Film()
    return render(request, 'coolapp/new.html',
                  {'form': FilmForm(instance=film)})
