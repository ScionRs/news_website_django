from django.shortcuts import render, get_object_or_404
from .models import News, Category
# Create your views here.

def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {'news': news, 'title': 'Список новостей', 'categories': categories}
    return render(request, 'news/index.html', context)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news,
                                                  'categories': categories,
                                                  'category': category})

def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    categories = Category.objects.all()
    return render(request, 'news/view_news.html', {'categories': categories, "news_item" : news_item})

