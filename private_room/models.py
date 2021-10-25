from django.contrib.auth.models import User
from django.db import models
# from django.urls import reverse
# Create your models here.
# from django.urls import reverse


class CategoriesOfCustomers(models.Model):
    customers_type = models.CharField('Категория клиента', max_length=2)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.customers_type

    class Meta:
        verbose_name = '''Категория клиента'''
        verbose_name_plural = '''Категория клиентов'''


class MotorcycleOrder(models.Model):  # PrivateRoomHome
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    # user_login_private_room = models.ForeignKey('UserLoginPrivateRoom', max_length=50, on_delete=models.PROTECT,
    #                                             verbose_name="Логин пользователя для личного кабинета")
    user = models.ForeignKey(User, max_length=50, on_delete=models.PROTECT,
                             verbose_name="Логин пользователя")
    categories_of_customers = models.ForeignKey('CategoriesOfCustomers', on_delete=models.PROTECT,
                                                verbose_name="Категория клиента")
    user_name_private_room = models.CharField('Имя клиента', max_length=50)
    user_surname_private_room = models.CharField('Фамилия клиента', max_length=50)
    customers_passport_series = models.CharField('Серия паспорта клиента', max_length=2)
    customers_passport_number = models.CharField('Номер паспорта клиента', max_length=7)
    customers_passport_id = models.CharField('Идентификационный номер паспорта клиента*', max_length=14)
    customers_enterprise_name = models.CharField('Наименование организации клиента', max_length=50, blank=True)
    moto_agreement_number = models.CharField('Номер договора*', max_length=30)
    moto_agreement_conclusion_date = models.DateField('Дата заключения договора*',)  # max_length=10
    # moto_vehicle_category = models.ForeignKey('MotoVehicleCategory', null=True, on_delete=models.PROTECT,
    #                                           verbose_name="Категория заказанной мототехники")
    moto_brand = models.ForeignKey('MotoBrand', max_length=50, on_delete=models.PROTECT,
                                   verbose_name="Марка мотоцикла")
    moto_release_date = models.DateField('Год выпуска заказанного мотоцикла', )  # max_length=10
    type_of_moto = models.ForeignKey('TypeOfMotorcycleCategory', null=True, on_delete=models.PROTECT,
                                     verbose_name="Тип заказанного мотоцикла")
    moto_engine_volume = models.CharField('Объем двигателя, см3', max_length=30)
    moto_engine_type = models.ForeignKey('MotoEngineType', null=True, on_delete=models.PROTECT,
                                         verbose_name="Вид топлива мотоцикла")
    moto_VIN_vehicle = models.CharField('VIN номер заказанного мотоцикла', max_length=17)
    moto_expected_delivery_date_in_the_RB = models.DateField('Ожидаемая дата прибытия заказанной техники',)
    moto_time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    moto_time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления заказа')

    def __str__(self):
        return self.user_name_private_room

    # def get_absolute_url(self):
        # return reverse('moto_import_order', kwargs={'moto_import_order_id': self.pk})
        # return reverse('post', kwargs={'post_id': self.pk})
        # ссылка self - это ссылка на ЭК Women
        # и, соотв-но, имея эту сссылку self мы можем брать любой атрибут текущей записи
        # в нашем случае возьмем атрибут 'pk'

    class Meta:
        verbose_name = '''ЗАКАЗ - Привоз мотоцикла'''
        verbose_name_plural = '''ЗАКАЗЫ - Привоз мотоциклов'''
        ordering = ['-moto_time_create', '-moto_agreement_conclusion_date', 'user_name_private_room',
                    'user_surname_private_room', 'customers_enterprise_name']


class AutoOrder(models.Model):  # PrivateRoomHome
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    # user_login_private_room = models.ForeignKey('UserLoginPrivateRoom', max_length=50, on_delete=models.PROTECT,
    #                                             verbose_name="Логин пользователя для личного кабинета")
    user = models.ForeignKey(User, max_length=50, on_delete=models.PROTECT,
                             verbose_name="Логин пользователя")
    categories_of_customers = models.ForeignKey('CategoriesOfCustomers', on_delete=models.PROTECT,
                                                verbose_name="Категория клиента")
    user_name_private_room = models.CharField('Имя клиента', max_length=50)
    user_surname_private_room = models.CharField('Фамилия клиента', max_length=50)
    customers_passport_series = models.CharField('Серия паспорта клиента', max_length=2)
    customers_passport_number = models.CharField('Номер паспорта клиента', max_length=7)
    customers_passport_id = models.CharField('Идентификационный номер паспорта клиента', max_length=14)
    customers_enterprise_name = models.CharField('Наименование организации клиента', max_length=50, blank=True)
    auto_agreement_number = models.CharField('Номер договора', max_length=30)
    auto_agreement_conclusion_date = models.DateField('Дата заключения договора',)  # max_length=10
    # auto_vehicle_category = models.ForeignKey('AutoVehicleCategory', null=True, on_delete=models.PROTECT,
    #                                           verbose_name="Категория заказанного автомобиля")
    auto_brand = models.ForeignKey('AutoBrand', max_length=50, on_delete=models.PROTECT,
                                   verbose_name="Марка автомобиля")
    auto_release_date = models.DateField('Год выпуска заказанного автомобиля', )  # max_length=10
    type_of_auto = models.ForeignKey('TypeOfAutoCategory', null=True, on_delete=models.PROTECT,
                                     verbose_name="Тип заказанного автомобиля")
    auto_engine_volume = models.CharField('Объем двигателя, см3', max_length=30)
    auto_engine_type = models.ForeignKey('AutoEngineType', null=True, on_delete=models.PROTECT,
                                         verbose_name="Вид топлива автомобиля")
    auto_VIN_vehicle = models.CharField('VIN номер заказанного автомобиля', max_length=17)
    auto_expected_delivery_date_in_the_RB = models.DateField('Ожидаемая дата прибытия заказанной техники',
                                                             )  # max_length=10
    auto_time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    auto_time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления заказа')

    def __str__(self):
        return self.user_name_private_room

    class Meta:
        verbose_name = '''ЗАКАЗ - Привоз автомобиля'''
        verbose_name_plural = '''ЗАКАЗЫ - Привоз автомобилей'''
        ordering = ['-auto_time_create', '-auto_agreement_conclusion_date', 'user_name_private_room',
                    'user_surname_private_room', 'customers_enterprise_name']


# -------   НОРМАЛИЗАЦИЯ ТАБЛИЦ С ЗАКАЗАМИ МОТОЦИКЛОВ И АВТО  ------- #

# -------   1. дополнение таблицы с мотозаказами (начало)   ------- #


class MotoBrand(models.Model):
    moto_brand_name = models.CharField(max_length=70, db_index=True, verbose_name='Наименование марки мотоцикла')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    # magic method - возвращает имя категории
    def __str__(self):
        return self.moto_brand_name

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Марка мотоцикла'
        verbose_name_plural = 'Марки мотоциклов'


class TypeOfMotorcycleCategory(models.Model):
    moto_type_name = models.CharField(max_length=70, db_index=True, verbose_name='Наименование класса мотоцикла')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    # magic method - возвращает имя категории
    def __str__(self):
        return self.moto_type_name

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Класс мотоцикла'
        verbose_name_plural = 'Классы мотоциклов'


class MotoEngineType(models.Model):
    moto_engine_type = models.CharField(max_length=70, db_index=True, verbose_name='Вид топлива мотоцикла')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    # magic method - возвращает имя категории
    def __str__(self):
        return self.moto_engine_type

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Вид топлива мотоцикла'
        verbose_name_plural = 'Виды топлива мотоциклов'
# -------   1. дополнение таблицы с мотозаказами (конец)   ------- #

# -------   2. дополнение таблицы с заказами авто (начало)   ------- #


class AutoBrand(models.Model):
    auto_brand_name = models.CharField(max_length=70, db_index=True, verbose_name='Наименование марки автомобиля')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    # magic method - возвращает имя категории
    def __str__(self):
        return self.auto_brand_name

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Марка автомобиля'
        verbose_name_plural = 'Марки автомобилей'


class TypeOfAutoCategory(models.Model):
    auto_type_name = models.CharField(max_length=70, db_index=True, verbose_name='Наименование класса автомобиля')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    # magic method - возвращает имя категории
    def __str__(self):
        return self.auto_type_name

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Класс автомобиля'
        verbose_name_plural = 'Классы автомобилей'


class AutoEngineType(models.Model):
    auto_engine_type = models.CharField(max_length=70, db_index=True, verbose_name='Вид топлива мотоцикла')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    # magic method - возвращает имя категории
    def __str__(self):
        return self.auto_engine_type

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Вид топлива автомобиля'
        verbose_name_plural = 'Виды топлива автомобилей'
# -------   2. дополнение таблицы с заказами авто (конец)   ------- #


###############################################
# ------- Ремонт мототехники (начало) ------- #
###############################################

class ServiceOrderMoto(models.Model):
    user = models.ForeignKey(User, max_length=50, on_delete=models.PROTECT,
                             verbose_name="Логин пользователя")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    categories_of_customers = models.ForeignKey('CategoriesOfCustomers', on_delete=models.PROTECT,
                                                verbose_name="Категория клиента")
    user_name_private_room = models.CharField('Имя клиента', max_length=50, blank=True)
    user_surname_private_room = models.CharField('Фамилия клиента', max_length=50, blank=True)
    customers_passport_series = models.CharField('Серия паспорта клиента', max_length=2, blank=True)
    customers_passport_number = models.CharField('Номер паспорта клиента', max_length=7, blank=True)
    customers_passport_id = models.CharField('Идентификационный номер паспорта клиента', max_length=14, blank=True)
    customers_enterprise_name = models.CharField('Наименование организации клиента', max_length=50, blank=True)
    moto_agreement_number = models.CharField('Номер договора', max_length=30, blank=True)
    moto_agreement_conclusion_date = models.DateField('Дата заключения договора', blank=True)
    moto_types_of_services = models.ForeignKey('MotoTypesOfServices', null=True, on_delete=models.PROTECT,
                                               verbose_name='Виды сервисных работ для мотоциклов')
    moto_brand = models.ForeignKey('MotoBrand', max_length=50, on_delete=models.PROTECT,
                                   verbose_name="Марка мотоцикла", blank=True)
    moto_release_date = models.DateField('Год выпуска мотоцикла в ремонте', blank=True)
    type_of_moto = models.ForeignKey('TypeOfMotorcycleCategory', null=True, on_delete=models.PROTECT,
                                     verbose_name="Тип мотоцикла в ремонте", blank=True)
    moto_engine_volume = models.CharField('Объем двигателя, см3', max_length=30, blank=True)
    moto_engine_type = models.ForeignKey('MotoEngineType', null=True, on_delete=models.PROTECT,
                                         verbose_name="Вид топлива мотоцикла", blank=True)
    moto_VIN_vehicle = models.CharField('VIN номер мотоцикла в ремонте', max_length=17, blank=True)
    moto_expected_result_service_date = models.DateField('Ожидаемая дата окончания ремонта техники', blank=True)
    moto_time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    moto_time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления заказа')

    def __str__(self):
        return self.user_name_private_room

    class Meta:
        verbose_name = '''ЗАКАЗ - Ремонт мотоцикла'''
        verbose_name_plural = '''ЗАКАЗЫ - Ремонт мотоциклов'''
        ordering = ['-moto_time_create', '-moto_agreement_conclusion_date', 'user_name_private_room',
                    'user_surname_private_room', 'customers_enterprise_name']


class MotoTypesOfServices(models.Model):
    moto_types_of_services = models.CharField(max_length=70, db_index=True, verbose_name='Виды сервисных работ для '
                                                                                         'мотоциклов')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    # magic method - возвращает имя категории
    def __str__(self):
        return self.moto_types_of_services

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Виды сервисных работ для мотоциклов'
        verbose_name_plural = 'Виды сервисных работ для мотоциклов'


class ServiceOrderAuto(models.Model):
    user = models.ForeignKey(User, max_length=50, on_delete=models.PROTECT,
                             verbose_name="Логин пользователя")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    categories_of_customers = models.ForeignKey('CategoriesOfCustomers', on_delete=models.PROTECT,
                                                verbose_name="Категория клиента")
    user_name_private_room = models.CharField('Имя клиента', max_length=50, blank=True)
    user_surname_private_room = models.CharField('Фамилия клиента', max_length=50, blank=True)
    customers_passport_series = models.CharField('Серия паспорта клиента', max_length=2, blank=True)
    customers_passport_number = models.CharField('Номер паспорта клиента', max_length=7, blank=True)
    customers_passport_id = models.CharField('Идентификационный номер паспорта клиента', max_length=14, blank=True)
    customers_enterprise_name = models.CharField('Наименование организации клиента', max_length=50, blank=True)
    auto_agreement_number = models.CharField('Номер договора', max_length=30, blank=True)
    auto_agreement_conclusion_date = models.DateField('Дата заключения договора', blank=True)  # max_length=10
    # нужно добавить модель категорию техники -----------------  НАДО ЛИ???????????????????
    # vehicle_category = models.ForeignKey('VehicleCategory', null=True, on_delete=models.PROTECT, )
    # #                                           verbose_name="Категория заказанного автомобиля")
    auto_types_of_services = models.ForeignKey('AutoTypesOfServices', null=True, on_delete=models.PROTECT,
                                               verbose_name='Виды сервисных работ для автомобилей')
    auto_brand = models.ForeignKey('AutoBrand', max_length=50, on_delete=models.PROTECT,
                                   verbose_name="Марка автомобиля", blank=True)
    auto_release_date = models.DateField('Год выпуска автомобиля в ремонте', blank=True)  # max_length=10
    type_of_auto = models.ForeignKey('TypeOfMotorcycleCategory', null=True, on_delete=models.PROTECT,
                                     verbose_name="Тип автомобиля в ремонте", blank=True)
    auto_engine_volume = models.CharField('Объем двигателя, см3', max_length=30, blank=True)
    auto_engine_type = models.ForeignKey('AutoEngineType', null=True, on_delete=models.PROTECT,
                                         verbose_name="Вид топлива автомобиля", blank=True)
    auto_VIN_vehicle = models.CharField('VIN номер автомобиля в ремонте', max_length=17, blank=True)
    auto_expected_result_service_date = models.DateField('Ожидаемая дата окончания ремонта техники', blank=True)
    auto_time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    auto_time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления заказа')

    def __str__(self):
        return self.user_name_private_room

    class Meta:
        verbose_name = '''ЗАКАЗ - Ремонт автомобиля'''
        verbose_name_plural = '''ЗАКАЗЫ - Ремонт автомобилей'''
        ordering = ['-auto_time_create', '-auto_agreement_conclusion_date', 'user_name_private_room',
                    'user_surname_private_room', 'customers_enterprise_name']


class AutoTypesOfServices(models.Model):
    auto_types_of_services = models.CharField(max_length=70, db_index=True, verbose_name='Виды сервисных работ для '
                                                                                         'автомобилей')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    # magic method - возвращает имя категории
    def __str__(self):
        return self.auto_types_of_services

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Виды сервисных работ для автомобилей'
        verbose_name_plural = 'Виды сервисных работ для автомобилей'

###############################################
# ------- Ремонт мототехники (конец) ------- #
###############################################

########################################
# ------- Хранение мототехники ------- #
########################################


class MotoSafekeeping(models.Model):
    user = models.ForeignKey(User, max_length=50, on_delete=models.PROTECT,
                             verbose_name="Логин пользователя")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    categories_of_customers = models.ForeignKey('CategoriesOfCustomers', on_delete=models.PROTECT,
                                                verbose_name="Категория клиента")
    user_name_private_room = models.CharField('Имя клиента', max_length=50, blank=True)
    user_surname_private_room = models.CharField('Фамилия клиента', max_length=50, blank=True)
    customers_passport_series = models.CharField('Серия паспорта клиента', max_length=2, blank=True)
    customers_passport_number = models.CharField('Номер паспорта клиента', max_length=7, blank=True)
    customers_passport_id = models.CharField('Идентификационный номер паспорта клиента', max_length=14, blank=True)
    customers_enterprise_name = models.CharField('Наименование организации клиента', max_length=50, blank=True)
    moto_agreement_number = models.CharField('Номер договора', max_length=30, blank=True)
    moto_brand = models.ForeignKey('MotoBrand', max_length=50, on_delete=models.PROTECT,
                                   verbose_name="Марка мотоцикла", blank=True)
    moto_release_date = models.DateField('Год выпуска мотоцикла', blank=True)
    type_of_moto = models.ForeignKey('TypeOfMotorcycleCategory', null=True, on_delete=models.PROTECT,
                                     verbose_name="Тип мотоцикла", blank=True)
    moto_engine_volume = models.CharField('Объем двигателя, см3', max_length=30, blank=True)
    moto_engine_type = models.ForeignKey('MotoEngineType', null=True, on_delete=models.PROTECT,
                                         verbose_name="Вид топлива мотоцикла", blank=True)
    moto_VIN_vehicle = models.CharField('VIN номер мотоцикла', max_length=17, blank=True)
    photo_vehicle = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фото переданного на'
                                                                                'хранение мотоцикла')
    moto_agreement_conclusion_date = models.DateField('Дата заключения договора', blank=True)
    moto_end_safekeeping_date = models.DateField('Дата окончания договора хранения', blank=True)
    moto_time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    moto_time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления заказа')

    def __str__(self):
        return self.user_name_private_room

    class Meta:
        verbose_name = '''ЗАКАЗ - Хранение мотоцикла'''
        verbose_name_plural = '''ЗАКАЗЫ - Хранение мотоциклов'''
        ordering = ['-moto_time_create', '-moto_agreement_conclusion_date', 'user_name_private_room',
                    'user_surname_private_room', 'customers_enterprise_name']
