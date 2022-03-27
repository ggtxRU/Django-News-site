from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', GetCategory.as_view(), name='category'),
    path('news/<int:pk>/', View_News.as_view(), name='view_news'),
    path('news/add_news/', Create_News.as_view(), name='add_news'),

]
