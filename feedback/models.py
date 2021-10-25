from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Feedback(models.Model):  # таблица в БД будет называться также
    author_name = models.CharField('Имя автора', max_length=50)
    #slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    # author_name = models.ForeignKey(User, max_length=50, on_delete=models.PROTECT,
    #                                 verbose_name="Логин пользователя")
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField('Текст отзыва', blank=True)  # blank=True - не обязательное поле
    author_photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фото', blank=True, null=True,
                                     default='main/img/icon_quality_v2.png')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания отзыва')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления отзыва')
    # email_is_active = models.BooleanField(default=False, verbose_name='Подтверждение через email')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    agreement_number = models.CharField('Номер договора', max_length=15)
    feedback_category = models.ForeignKey('ServiceCategory', null=True, on_delete=models.PROTECT,
                                          verbose_name="Категория услуг")

    def __str__(self):
        return str(self.author_name)

    def get_absolute_url(self):
        return reverse('feedback-detail', kwargs={'feedback_add_by_customer_id': self.pk})

    class Meta:
        verbose_name = '''Отзыв'''
        verbose_name_plural = '''Отзывы'''
        ordering = ['-time_create', 'author_name']

class ServiceCategory(models.Model):
    service_category_name = models.CharField(max_length=100, db_index=True, verbose_name='Наименование категории услуг')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    # magic method - возвращает имя категории
    def __str__(self):
        return self.service_category_name

    def get_absolute_url(self):
        return reverse('service_category', kwargs={'feedback_category_id': self.pk})

    class Meta:
        verbose_name = '''Категория услуг'''
        verbose_name_plural = '''Категории услуг'''
