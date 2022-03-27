
from django.views.generic import ListView, DetailView, CreateView

from .models import News, Category
from .forms import NewsForm
from django.core.paginator import Paginator

class HomeNews(ListView):
    """Класс, отвечающий за обработку главной страницы с новостями."""
    model = News
    """Определяем модель из которой будем получать данные
	В данном случае получаем все данные из модели News"""
    template_name = 'news/index.html'
    """Определяем шаблон"""
    context_object_name = 'news'
    """Определяем контекст объекта откуда будем брать данные в шаблоне"""
    """Добавляем пагинацию"""
    paginate_by = 2

    def get_context_data(self, **kwargs):
        """Определяем контекст."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        """Поправляем запрос в БД, добавляем фильтрацию на вывод."""
        return News.objects.order_by('-created_at').filter(is_published=True).select_related('category')


class GetCategory(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False
    'Аналог get_object_or_404'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        """Определяем контекст."""
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        context['category'] = Category.objects.get(
            pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        """Поправляем запрос в БД, добавляем фильтрацию на вывод, также
        добавляем привязку к категории."""
        return News.objects.order_by('-created_at').filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class View_News(DetailView):
    """Класс, предназначенный для показа отдельно взятой новости."""
    model = News
    template_name = 'news/view_news.html'
    context_object_name = 'news_item'


class Create_News(CreateView):
    """Класс для работы с формой создания новой новости."""
    form_class = NewsForm
    template_name = 'news/add_news.html'
