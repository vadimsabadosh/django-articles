from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Category
from .forms import NewsForm
from django.views.generic import ListView, DetailView, CreateView


# Class Controllers
class HomeViews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Головна сторінка'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsByCategory(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class ViewNews(DetailView):
    model = News
    template_name = 'news/news_item.html'
    # pk_url_kwarg = "news_id"
    context_object_name = 'news_item'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'

# Function controllers

def index(request):
    news = News.objects.all()
    context = {'news': news, 'title': 'Список новин'}
    return render(request, 'news/index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {'news': news, 'category': category}
    return render(request, 'news/category.html', context)


def get_news(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    context = {'news_item': news}
    return render(request, 'news/news_item.html', context)


def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {"form": form})
