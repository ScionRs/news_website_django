from django.db import models
from django.urls import reverse

# Create your models here.

class News(models.Model):
    header = models.CharField(verbose_name='Заголовок статьи')
    photo_link = models.CharField(verbose_name='Ссылка')
    content = models.TextField(blank=True, verbose_name='Содержимое')
    article_link = models.CharField(verbose_name='Ссылка на оригинал')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'news_id': self.pk})

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'





class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Категория")

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
