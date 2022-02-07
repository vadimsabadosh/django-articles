from django.urls import path

from news.views import *

urlpatterns = [
    # path('', index, name="home"),
    path('', HomeViews.as_view(), name="home"),
    # path('category/<int:category_id>/', get_category, name="category"),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name="category"),
    # path('news/<int:news_id>/', get_news, name="news_item"),
    path('news/<int:pk>/', ViewNews.as_view(), name="news_item"),
    # path('news/add-news/', add_news, name="add-news"),
    path('news/add-news/', CreateNews.as_view(), name="add-news"),
]
