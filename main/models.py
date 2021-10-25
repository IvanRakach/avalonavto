# from django.db import models
# from autoslug import AutoSlugField
from django.urls import reverse
from private_room.models import *
# Create your models here.


class ContactWithUs(models.Model):
    # login_field =
    name_field = models.CharField('Имя пользователя', max_length=50)  # , verbose_name="Имя пользователя"
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    email_field = models.CharField('Email пользователя', max_length=50)
    content_field = models.TextField('Текст заданного вопроса', max_length=1000)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата обращения пользователя')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления обращения пользователя')

    def __str__(self):
        return self.name_field

    # def get_absolute_url(self):  # self - это ЭК Feedback и имея эту ссылку self мы
    #                              # можем брать любой атрибут текущей записи, например возьмем 'pk'
    #                              # такие ссылки лучше делать, если есть связь с БД
    #     return reverse('feedback-detail', kwargs={'pk': self.pk})  # f'/feedback/{self.id}'

    class Meta:
        verbose_name = '''Форма: Свяжитесь с нами'''
        verbose_name_plural = '''Форма: Свяжитесь с нами'''
        ordering = ['-time_create', 'name_field']


class AvailableCars(models.Model):
    auto_brand_title_field = models.ForeignKey('private_room.AutoBrand', max_length=50, on_delete=models.PROTECT,
                                               verbose_name="Марка автомобиля")
    auto_model_title_field = models.CharField('Модель автомобиля', max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    auto_type = models.ForeignKey('private_room.TypeOfAutoCategory', null=True, on_delete=models.PROTECT,
                                  verbose_name="Тип заказанного автомобиля")
    fuel_type_field = models.ForeignKey('private_room.AutoEngineType', null=True, on_delete=models.PROTECT,
                                        verbose_name="Вид топлива автомобиля")
    eng_vol_field = models.CharField('Объем двигателя', max_length=10)
    auto_mileage_field = models.CharField('Пробег', max_length=15)  # car_mileage_field
    transmission_field = models.ForeignKey('TransmissionCategory', null=True, on_delete=models.PROTECT,
                                           verbose_name="Вид трансмиссии")
    auto_release_date_field = models.CharField('Год выпуска автомобиля', max_length=4)
    auto_VIN_vehicle = models.CharField('VIN номер автомобиля', max_length=17)
    auto_description_field = models.TextField('Текст объявления', blank=True)
    auto_image_field_main = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография главная',)
    auto_image_field_2 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 2',)  # blank=True
    auto_image_field_3 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 3',)  # blank=True
    auto_image_field_4 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 4', blank=True)
    auto_image_field_5 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 5', blank=True)
    auto_image_field_6 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 6', blank=True)
    auto_image_field_7 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 7', blank=True)
    auto_image_field_8 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 8', blank=True)
    auto_image_field_9 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 9', blank=True)
    auto_image_field_10 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 10', blank=True)
    auto_image_field_11 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 11', blank=True)
    auto_image_field_12 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 12', blank=True)
    auto_image_field_13 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 13', blank=True)
    auto_image_field_14 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 14', blank=True)
    auto_image_field_15 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 15', blank=True)
    auto_image_field_16 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 16', blank=True)
    auto_image_field_17 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 17', blank=True)
    auto_image_field_18 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 18', blank=True)
    auto_image_field_19 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 19', blank=True)
    auto_image_field_20 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 20', blank=True)
    auto_video_field_load = models.FileField(upload_to='videos/%Y/%m/%d',
                                        null=True, blank=True,
                                        verbose_name="Видео (прямая загрузка с сайта)")
    auto_video_field_youtube = models.CharField(null=True, verbose_name="Видео (через ссылку с YouTube)",
                                                blank=True, max_length=255)
    auto_price_BYN_field = models.PositiveIntegerField('Цена в BYN')  # , max_length=15
    auto_price_USD_field = models.PositiveIntegerField('Цена в USD')  # , max_length=15
    auto_location_field = models.CharField('Расположение', max_length=15)
    auto_contacts_field = models.CharField('Контакты', max_length=20)
    auto_link_field = models.URLField('Ссылка на автомобиль на av.by', blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания объявления')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления объявления')

    def __str__(self):
        return str(self.auto_brand_title_field)

    def get_absolute_url(self):
        # return reverse('moto_import_available_moto_offer', kwargs={'moto_import_available_moto_offer_id': self.pk})
        return reverse('auto_import_available_auto_offer', kwargs={'auto_import_available_auto_offer_slug': self.slug})
        # return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = '''Таблица: Имеющиеся в продаже автомобили'''
        verbose_name_plural = '''Таблица: Имеющиеся в продаже автомобили'''
        ordering = ['auto_brand_title_field', 'auto_price_BYN_field', 'auto_price_USD_field', '-time_create']


class AvailableMoto(models.Model):
    moto_brand_title_field = models.ForeignKey('private_room.MotoBrand', max_length=50, on_delete=models.PROTECT,
                                               verbose_name="Марка мотоцикла")
    moto_model_title_field = models.CharField('Модель мотоцикла', max_length=50)
    # ##########################################################################
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL (slug)")
    # ##########################################################################
    type_of_moto = models.ForeignKey('private_room.TypeOfMotorcycleCategory', null=True, on_delete=models.PROTECT,
                                     verbose_name="Тип заказанного мотоцикла")
    fuel_type_field = models.ForeignKey('private_room.MotoEngineType', null=True, on_delete=models.PROTECT,
                                        verbose_name="Вид топлива мотоцикла")
    eng_vol_field = models.CharField('Объем двигателя', max_length=10)
    moto_mileage_field = models.CharField('Пробег', max_length=15)
    transmission_field = models.ForeignKey('TransmissionCategory', null=True, on_delete=models.PROTECT,
                                           verbose_name="Вид трансмиссии")
    moto_release_date_field = models.CharField('Год выпуска мотоцикла', max_length=4)
    moto_VIN_vehicle = models.CharField('VIN номер мотоцикла', max_length=17)
    moto_description_field = models.TextField('Текст объявления', blank=True)
    moto_image_field_main = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография главная',)
    moto_image_field_2 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 2',)  # blank=True
    moto_image_field_3 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 3',)  # blank=True
    moto_image_field_4 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 4', blank=True)
    moto_image_field_5 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 5', blank=True)
    moto_image_field_6 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 6',
                                           blank=True)
    moto_image_field_7 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 7',
                                           blank=True)
    moto_image_field_8 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 8',
                                           blank=True)
    moto_image_field_9 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 9',
                                           blank=True)
    moto_image_field_10 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 10',
                                            blank=True)
    moto_image_field_11 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 11',
                                            blank=True)
    moto_image_field_12 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 12',
                                            blank=True)
    moto_image_field_13 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 13',
                                            blank=True)
    moto_image_field_14 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 14',
                                            blank=True)
    moto_image_field_15 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 15',
                                            blank=True)
    moto_image_field_16 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 16',
                                            blank=True)
    moto_image_field_17 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 17',
                                            blank=True)
    moto_image_field_18 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 18',
                                            blank=True)
    moto_image_field_19 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 19',
                                            blank=True)
    moto_image_field_20 = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография 20',
                                            blank=True)
    moto_video_field_load = models.FileField(upload_to='videos/%Y/%m/%d',
                                             null=True, blank=True,
                                             verbose_name="Видео (прямая загрузка с сайта)")
    moto_video_field_youtube = models.CharField(null=True, verbose_name="Видео (через ссылку с YouTube)",
                                                blank=True, max_length=255)
    moto_price_BYN_field = models.PositiveIntegerField('Цена в BYN')  # , max_length=15
    moto_price_USD_field = models.PositiveIntegerField('Цена в USD')  # , max_length=15
    moto_location_field = models.CharField('Расположение', max_length=15)
    moto_contacts_field = models.CharField('Контакты', max_length=20)
    moto_link_field = models.URLField('Ссылка на мотоцикл на сайте av.by', blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания объявления')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления объявления')

    def __str__(self):
        return str(self.moto_brand_title_field)

    def get_absolute_url(self):
        # return reverse('moto_import_available_moto_offer', kwargs={'moto_import_available_moto_offer_id': self.pk})
        return reverse('moto_import_available_moto_offer', kwargs={'moto_import_available_moto_offer_slug': self.slug})
        # return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = '''Таблица: Имеющиеся в продаже мотоциклы'''
        verbose_name_plural = '''Таблица: Имеющиеся в продаже мотоциклы'''
        ordering = ['moto_brand_title_field', 'moto_price_BYN_field', 'moto_price_USD_field', '-time_create']


class TransmissionCategory(models.Model):
    transmission_field = models.CharField('Вид трансмиссии', max_length=15)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    # magic method - возвращает имя категории
    def __str__(self):
        return self.transmission_field

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Дополнение: Вид трансмиссии'
        verbose_name_plural = 'Дополнение: Вид трансмиссий'


# ##################################################################################### #
from django.utils import timezone

# IP-адрес и количество посещений сайта
class Userip(models.Model):
    ip = models.CharField(verbose_name='Айпи адрес', max_length=30)    #айпи адрес
    count = models.IntegerField(verbose_name='Визиты', default=0) # Ip посещения

    class Meta:
        verbose_name = 'Доступ к информации о пользователе'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip

# Всего посещений сайта
class VisitNumber(models.Model):
    count = models.IntegerField(verbose_name='Всего посещений сайта', default=0)  # Всего посещений сайта

    class Meta:
        verbose_name = 'Всего посещений сайта'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.count)

# Статистика посещений за один день
class DayNumber(models.Model):
    day = models.DateField(verbose_name='Дата', default=timezone.now)
    count = models.IntegerField(verbose_name='Количество посещений сайта', default=0)  # Всего посещений сайта

    class Meta:
        verbose_name = 'Статистика ежедневных посещений сайта'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.day)
