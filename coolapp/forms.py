from django import forms
from .models import Film


class FilmForm(forms.ModelForm):
    """
    Этот класс будет управлять отображением таблички с фильмами для пользователей
    """
    class Meta:
        model = Film
        fields = ('name', 'desc', 'rate', 'comments')


# поля pub_date и id заполняются сами
