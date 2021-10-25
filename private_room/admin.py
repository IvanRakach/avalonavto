from django.contrib import admin

# Register your models here.
from .models import *

######################################################################
# -------------   Блок: категория клиентов (начало)   -------------- #
######################################################################


class CategoriesOfCustomersAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('id', 'customers_type',)
    # те поля, на которые мы можем кликнуть и перейти на соответствующий заказ
    list_display_links = ('id', 'customers_type',)
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('customers_type',)  # это кортеж! не забываем!
    # автоматическое заполнение слага
    prepopulated_fields = {"slug": ("customers_type",)}


admin.site.register(CategoriesOfCustomers, CategoriesOfCustomersAdmin)

######################################################################
# -------------   Блок: категория клиентов (конец)   -------------- #
######################################################################

######################################################################
# ------   Блок: Таблицы заказов мотоциклов и авто (начало)   ------ #
######################################################################
# ------------------------------------------------------------------ #
#                   Таблица: заказ мотоцикла (начало)                #
# ------------------------------------------------------------------ #


class MotorcycleOrderAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('user', 'user_name_private_room', 'user_surname_private_room', 'customers_passport_series',
                    'customers_passport_number', 'customers_passport_id', 'categories_of_customers',
                    'customers_enterprise_name', 'moto_agreement_number', 'moto_agreement_conclusion_date',
                    'moto_brand', 'moto_release_date', 'type_of_moto', 'moto_engine_volume', 'moto_engine_type',
                    'moto_VIN_vehicle', 'moto_expected_delivery_date_in_the_RB', 'moto_time_create', 'moto_time_update')
    # те поля, на которые мы можем кликнуть и перейти на соответствующий заказ
    list_display_links = ('user', 'user_name_private_room', 'user_surname_private_room', 'categories_of_customers',
                          'customers_enterprise_name', 'moto_agreement_number')
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('user', 'user_name_private_room', 'user_surname_private_room', 'categories_of_customers',
                     'customers_enterprise_name', 'moto_agreement_number', 'moto_VIN_vehicle')
    # те поля, которые мы можем редактировать в списке самих комментариев
    # list_editable = ('is_published',)
    # те поля, по которым мы можем фильтровать список статей
    list_filter = ('user', 'categories_of_customers', 'moto_brand', 'moto_engine_type', 'moto_time_create',
                   'user_surname_private_room', 'customers_enterprise_name',)


admin.site.register(MotorcycleOrder, MotorcycleOrderAdmin)


class MotoBrandAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('id', 'moto_brand_name', 'slug')
    # те поля, на которые мы можем кликнуть и перейти на соответствующий заказ
    list_display_links = ('id', 'moto_brand_name', 'slug')
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('moto_brand_name',)  # это кортеж! не забываем!
    # автоматическое заполнение слага
    prepopulated_fields = {"slug": ("moto_brand_name",)}


admin.site.register(MotoBrand, MotoBrandAdmin)


class TypeOfMotorcycleCategoryAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('id', 'moto_type_name', 'slug')
    # те поля, на которые мы можем кликнуть и перейти на соответствующий заказ
    list_display_links = ('id', 'moto_type_name', 'slug')
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('moto_type_name',)  # это кортеж! не забываем!
    # автоматическое заполнение слага
    prepopulated_fields = {"slug": ("moto_type_name",)}


admin.site.register(TypeOfMotorcycleCategory, TypeOfMotorcycleCategoryAdmin)


class MotoEngineTypeAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('id', 'moto_engine_type', 'slug')
    # те поля, на которые мы можем кликнуть и перейти на соответствующий заказ
    list_display_links = ('id', 'moto_engine_type', 'slug')
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('moto_type_name',)  # это кортеж! не забываем!
    # автоматическое заполнение слага
    prepopulated_fields = {"slug": ("moto_engine_type",)}

admin.site.register(MotoEngineType, MotoEngineTypeAdmin)
# ------------------------------------------------------------------ #
#                   Таблица: заказ мотоцикла (конец)                 #
# ------------------------------------------------------------------ #

# ------------------------------------------------------------------ #
#                  Таблица: заказ автомобиля (начало)                #
# ------------------------------------------------------------------ #


class AutoOrderAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('user', 'user_name_private_room', 'user_surname_private_room', 'customers_passport_series',
                    'customers_passport_number',  'customers_passport_id', 'categories_of_customers', 'customers_enterprise_name',
                    'auto_agreement_number', 'auto_agreement_conclusion_date', 'auto_brand', 'auto_release_date',
                    'type_of_auto', 'auto_engine_volume', 'auto_engine_type', 'auto_VIN_vehicle',
                    'auto_expected_delivery_date_in_the_RB', 'auto_time_create', 'auto_time_update')
    # те поля, на которые мы можем кликнуть и перейти на соответствующий заказ
    list_display_links = ('user', 'user_name_private_room', 'user_surname_private_room', 'categories_of_customers', 'customers_enterprise_name',
                          'auto_agreement_number')
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('user', 'user_name_private_room', 'user_surname_private_room', 'categories_of_customers', 'customers_enterprise_name',
                     'auto_agreement_number', 'auto_VIN_vehicle')
    # те поля, которые мы можем редактировать в списке самих комментариев
    # list_editable = ('is_published',)
    # те поля, по которым мы можем фильтровать список статей
    list_filter = ('user', 'auto_brand', 'auto_engine_type', 'auto_time_create', 'categories_of_customers', 'user_surname_private_room',
                   'customers_enterprise_name',)


admin.site.register(AutoOrder, AutoOrderAdmin)


class AutoBrandAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('id', 'auto_brand_name', 'slug')
    # те поля, на которые мы можем кликнуть и перейти на соответствующий заказ
    list_display_links = ('id', 'auto_brand_name', 'slug')
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('auto_brand_name',)  # это кортеж! не забываем!
    # автоматическое заполнение слага
    prepopulated_fields = {"slug": ("auto_brand_name",)}


admin.site.register(AutoBrand, AutoBrandAdmin)


class TypeOfAutoCategoryAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('id', 'auto_type_name', 'slug')
    # те поля, на которые мы можем кликнуть и перейти на соответствующий заказ
    list_display_links = ('id', 'auto_type_name', 'slug')
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('auto_type_name',)  # это кортеж! не забываем!
    # автоматическое заполнение слага
    prepopulated_fields = {"slug": ("auto_type_name",)}


admin.site.register(TypeOfAutoCategory, TypeOfAutoCategoryAdmin)


class AutoEngineTypeAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('id', 'auto_engine_type', 'slug')
    # те поля, на которые мы можем кликнуть и перейти на соответствующий заказ
    list_display_links = ('id', 'auto_engine_type', 'slug')
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('auto_type_name',)  # это кортеж! не забываем!
    # автоматическое заполнение слага
    prepopulated_fields = {"slug": ("auto_engine_type",)}


admin.site.register(AutoEngineType, AutoEngineTypeAdmin)

# ------------------------------------------------------------------ #
#                  Таблица: заказ автомобиля (конец)                 #
# ------------------------------------------------------------------ #
######################################################################
# ------   Блок: Таблицы заказов мотоциклов и авто (конец)    ------ #
######################################################################

######################################################################
# ------    Блок: Таблицы Ремонт мотоциклов и авто (начало)   ------ #
######################################################################
# ------------------------------------------------------------------ #
#                     Таблица: ремонт мото (начало)                  #
# ------------------------------------------------------------------ #


class ServiceOrderMotoAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('user', 'user_name_private_room', 'user_surname_private_room', 'customers_passport_series',
                    'customers_passport_number', 'customers_passport_id', 'categories_of_customers', 'customers_enterprise_name',
                    'moto_agreement_number', 'moto_agreement_conclusion_date', 'moto_types_of_services', 'moto_brand',
                    'moto_release_date', 'type_of_moto', 'moto_engine_volume', 'moto_engine_type', 'moto_VIN_vehicle',
                    'moto_expected_result_service_date', 'moto_time_create', 'moto_time_update',)
    # те поля, на которые мы можем кликнуть и перейти на соответствующий заказ
    list_display_links = ('user', 'user_name_private_room', 'user_surname_private_room', 'categories_of_customers', 'customers_enterprise_name',
                          'moto_agreement_number')
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('user', 'user_name_private_room', 'user_surname_private_room', 'categories_of_customers', 'moto_agreement_number',
                     'customers_enterprise_name', 'moto_VIN_vehicle')
    # те поля, которые мы можем редактировать в списке самих комментариев
    # list_editable = ('is_published',)
    # те поля, по которым мы можем фильтровать список статей
    list_filter = ('user', 'categories_of_customers', 'moto_types_of_services', 'moto_brand', 'moto_engine_type', 'moto_time_create',
                   'user_surname_private_room', 'customers_enterprise_name',)


admin.site.register(ServiceOrderMoto, ServiceOrderMotoAdmin)


class MotoTypesOfServicesAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('id', 'moto_types_of_services', 'slug')
    # те поля, на которые мы можем кликнуть и перейти на соответствующий заказ
    list_display_links = ('id', 'moto_types_of_services', 'slug')
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('moto_types_of_services',)  # это кортеж! не забываем!
    # автоматическое заполнение слага
    prepopulated_fields = {"slug": ("moto_types_of_services",)}


admin.site.register(MotoTypesOfServices, MotoTypesOfServicesAdmin)
# ------------------------------------------------------------------ #
#                     Таблица: ремонт мото (конец)                   #
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
#                  Таблица: ремонт автомобиля (начало)               #
# ------------------------------------------------------------------ #


class ServiceOrderAutoAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('user', 'user_name_private_room', 'user_surname_private_room', 'customers_passport_series',
                    'customers_passport_number', 'customers_passport_id', 'categories_of_customers', 'customers_enterprise_name',
                    'auto_agreement_number', 'auto_agreement_conclusion_date', 'auto_types_of_services', 'auto_brand',
                    'auto_release_date', 'type_of_auto', 'auto_engine_volume', 'auto_engine_type', 'auto_VIN_vehicle',
                    'auto_expected_result_service_date', 'auto_time_create', 'auto_time_update',)
    # те поля, на которые мы можем кликнуть и перейти на соответствующий заказ
    list_display_links = ('user', 'user_name_private_room', 'user_surname_private_room', 'categories_of_customers', 'customers_enterprise_name',
                          'auto_agreement_number')
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('user', 'user_name_private_room', 'user_surname_private_room', 'categories_of_customers', 'auto_agreement_number',
                     'customers_enterprise_name', 'auto_VIN_vehicle')
    # те поля, которые мы можем редактировать в списке самих комментариев
    # list_editable = ('is_published',)
    # те поля, по которым мы можем фильтровать список статей
    list_filter = ('user', 'categories_of_customers', 'auto_types_of_services', 'auto_brand', 'auto_engine_type', 'auto_time_create',
                   'user_surname_private_room', 'customers_enterprise_name',)


admin.site.register(ServiceOrderAuto, ServiceOrderAutoAdmin)


class AutoTypesOfServicesAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('id', 'auto_types_of_services', 'slug')
    # те поля, на которые мы можем кликнуть и перейти на соответствующий заказ
    list_display_links = ('id', 'auto_types_of_services', 'slug')
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('auto_types_of_services',)  # это кортеж! не забываем!
    # автоматическое заполнение слага
    prepopulated_fields = {"slug": ("auto_types_of_services",)}


admin.site.register(AutoTypesOfServices, AutoTypesOfServicesAdmin)
# ------------------------------------------------------------------ #
#                  Таблица: ремонт автомобиля (конец)                #
# ------------------------------------------------------------------ #
######################################################################
# ------       Блок: Таблица хранение мотоциклов (начало)     ------ #
######################################################################


class MotoSafekeepingAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('user', 'user_name_private_room', 'user_surname_private_room', 'customers_passport_series',
                    'customers_passport_number', 'customers_passport_id', 'categories_of_customers', 'customers_enterprise_name',
                    'moto_agreement_number', 'moto_brand', 'moto_release_date', 'type_of_moto', 'moto_engine_volume',
                    'moto_engine_type', 'moto_VIN_vehicle', 'photo_vehicle', 'moto_agreement_conclusion_date',
                    'moto_end_safekeeping_date', 'moto_time_create', 'moto_time_update',)
    # те поля, на которые мы можем кликнуть и перейти на соответствующий заказ
    list_display_links = ('user', 'user_name_private_room', 'user_surname_private_room', 'categories_of_customers', 'customers_enterprise_name',
                          'moto_agreement_number')
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('user', 'user_name_private_room', 'user_surname_private_room', 'categories_of_customers', 'moto_agreement_number',
                     'customers_enterprise_name', 'moto_VIN_vehicle')
    # те поля, которые мы можем редактировать в списке самих комментариев
    # list_editable = ('is_published',)
    # те поля, по которым мы можем фильтровать список статей
    list_filter = ('user', 'categories_of_customers', 'moto_brand', 'moto_engine_type', 'moto_time_create',
                   'user_surname_private_room', 'customers_enterprise_name',)


admin.site.register(MotoSafekeeping, MotoSafekeepingAdmin)
######################################################################
# ------       Блок: Таблица хранение мотоциклов (конец)      ------ #
######################################################################
