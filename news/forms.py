from distutils.command.upload import upload
from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError


"""Создаем форму добавления новой записи"""


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        """Добавляем поля формы"""
        fields = ['title', 'content', 'is_published', 'category', 'photo']

        """Настраиваем отображение на странице"""
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            # 'photo': forms.FileInput()
        }

    def clean_title(self):
        """Дополнительная валидация для title."""

        title = self.cleaned_data['title']
        """Получаем очишенные данные по ключу title ---> провалидированное на основе первичной валидации models"""

        if re.match(r'\d', title):
            """Ищем в начале строки цифры, если будет найдена цифра для title
            --> исключение, метод is_valid прекратит сохранять данные."""
            raise ValidationError('Название не может начинаться с цифры')

        """Если прошли проверку"""
        return title
