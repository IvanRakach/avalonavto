from django.contrib import admin

# Register your models here.

from .models import *
from .forms import *

# создадим вспомогательный класс для отображения большего количества столбцов в админ панели


class ContactWithUsAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('id', 'name_field', 'email_field', 'content_field', )  # 'is_published'
    # те поля, на которые мы можем кликнуть и перейти на соответствующий отзыв
    list_display_links = ('id', 'name_field')
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('name_field', 'email_field', )
    # те поля, которые мы можем редактировать в списке самих комментариев
    # list_editable = ('is_published',)
    # те поля, по которым мы можем фильтровать список статей
    list_filter = ('time_create',)  # 'is_published',


admin.site.register(ContactWithUs, ContactWithUsAdmin)


class AvailableCarsAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('id', 'auto_description_field',
                    'auto_contacts_field', 'auto_brand_title_field',
                    # 'auto_brand_title_field_slug',
                    'auto_model_title_field', 'slug',
                    'auto_link_field',
                    'auto_release_date_field', 'transmission_field', 'auto_type', 'fuel_type_field',
                    'eng_vol_field', 'auto_mileage_field', 'auto_VIN_vehicle', 'auto_price_BYN_field',
                    'auto_price_USD_field', 'auto_location_field',
                    'auto_image_field_main',
                    'auto_image_field_2',
                    'auto_image_field_3',
                    'auto_image_field_4',
                    'auto_image_field_5',
                    'auto_video_field_load',
                    'auto_video_field_youtube',
                    'time_create', 'time_update')  # 'is_published'
    # те поля, на которые мы можем кликнуть и перейти на соответствующий отзыв
    list_display_links = ('id', 'auto_image_field_main', 'auto_brand_title_field')
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('auto_brand_title_field', 'auto_model_title_field', 'auto_description_field')
    # те поля, которые мы можем редактировать в списке самих комментариев
    # list_editable = ('is_published',)
    # те поля, по которым мы можем фильтровать список статей
    list_filter = ('auto_brand_title_field',)  # 'is_published', '-time_create',
    # автоматическое заполнение слага
    prepopulated_fields = {"slug": ("auto_brand_title_field", "auto_model_title_field")}
    form = AvailableCarsForm


admin.site.register(AvailableCars, AvailableCarsAdmin)


class AvailableMotoAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('id',
                    'moto_description_field', 'moto_contacts_field',
                    'moto_brand_title_field',
                    # 'moto_brand_title_field_slug',
                    'moto_model_title_field', 'slug',
                    'moto_link_field',
                    'moto_release_date_field', 'transmission_field', 'type_of_moto', 'fuel_type_field',
                    'eng_vol_field', 'moto_mileage_field', 'moto_VIN_vehicle', 'moto_price_BYN_field',
                    'moto_price_USD_field', 'moto_location_field',
                    'moto_image_field_main',
                    'moto_image_field_2',
                    'moto_image_field_3',
                    'moto_image_field_4',
                    'moto_image_field_5',
                    'moto_video_field_load',
                    'moto_video_field_youtube',
                    'time_create', 'time_update')  # 'is_published'
    # те поля, на которые мы можем кликнуть и перейти на соответствующий отзыв
    list_display_links = ('id', 'moto_image_field_main', 'moto_brand_title_field', 'moto_description_field')
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('moto_brand_title_field', 'moto_model_title_field', 'moto_description_field')
    # те поля, которые мы можем редактировать в списке самих комментариев
    # list_editable = ('is_published',)
    # те поля, по которым мы можем фильтровать список статей
    list_filter = ('moto_brand_title_field',)  # 'is_published', '-time_create',
    # автоматическое заполнение слага
    prepopulated_fields = {"slug": ("moto_brand_title_field", "moto_model_title_field")}
    form = AvailableMotoForm


admin.site.register(AvailableMoto, AvailableMotoAdmin)


class TransmissionCategoryAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('id', 'transmission_field')  # 'is_published'
    # те поля, на которые мы можем кликнуть и перейти на соответствующий отзыв
    list_display_links = ('id', 'transmission_field')
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('transmission_field',)
    # те поля, которые мы можем редактировать в списке самих комментариев
    # list_editable = ('is_published',)
    # те поля, по которым мы можем фильтровать список статей
    list_filter = ('transmission_field',)  # 'is_published',
    # автоматическое заполнение слага
    prepopulated_fields = {"slug": ("transmission_field",)}
    # form = AvailableMotoForm


admin.site.register(TransmissionCategory, TransmissionCategoryAdmin)


class UseripAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip', 'count')
    list_display_links = ('id', 'ip', 'count')
    search_fields = ('count', 'ip',)
    list_filter = ('count', 'ip',)

admin.site.register(Userip, UseripAdmin)

class VisitNumberAdmin(admin.ModelAdmin):
    list_display = ('id', 'count')
    list_display_links = ('id', 'count')
    search_fields = ('count', )
    list_filter = ('count', )

admin.site.register(VisitNumber, VisitNumberAdmin)

class DayNumberAdmin(admin.ModelAdmin):
    list_display = ('id', 'day', 'count')
    list_display_links = ('id', 'day', 'count')
    search_fields = ('count', 'day',)
    list_filter = ('count', 'day',)

admin.site.register(DayNumber, DayNumberAdmin)