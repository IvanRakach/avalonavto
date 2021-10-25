from django.contrib import admin

# Register your models here.

from .models import *

# регистрация уже созданной модели, НО регистрируем уже после вспомогательных классов:
# admin.site.register(Feedback, FeedbackAdmin)
# admin.site.register(ServiceCategory)


# создадим вспомогательный класс для отображения большего количества столбцов в админ панели
class FeedbackAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('id', 'author_name',  'time_create', 'author_photo', 'feedback_category', 'is_published')  # 'slug',
    # те поля, на которые мы можем кликнуть и перейти на соответствующий отзыв
    list_display_links = ('id', 'author_name')
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('author_name', 'agreement_number', 'content', 'feedback_category')
    # те поля, которые мы можем редактировать в списке самих комментариев
    list_editable = ('is_published',)
    # те поля, по которым мы можем фильтровать список статей
    list_filter = ('is_published', 'time_create', 'feedback_category')
    # автоматическое заполнение слага
    # prepopulated_fields = {"slug": ("author_name", 'feedback_category')}


admin.site.register(Feedback, FeedbackAdmin)


class ServiceCategoryAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('id', 'service_category_name', 'slug')
    # те поля, на которые мы можем кликнуть и перейти на соответствующий отзыв
    list_display_links = ('id', 'service_category_name')
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('service_category_name',)  # это кортеж! не забываем!
    # автоматическое заполнение слага
    prepopulated_fields = {"slug": ("service_category_name",)}


admin.site.register(ServiceCategory, ServiceCategoryAdmin)
