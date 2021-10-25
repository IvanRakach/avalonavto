from django import forms
from .models import *
from private_room.models import *


class ContactWithUsForm(forms.ModelForm):

    class Meta:
        model = ContactWithUs
        fields = ['name_field', 'email_field', 'content_field']

        widgets = {
            'name_field': forms.TextInput(attrs={'class': 'form-control-mine', 'placeholder': 'Укажите Ваше имя'}),
            'email_field': forms.TextInput(attrs={'class': 'form-control-mine', 'placeholder': 'Укажите Ваш email'}),
            # 'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'content_field': forms.Textarea(attrs={'class': 'form-control-mine-content', 'placeholder': 'Опишите вопрос'})  # attrs={'class': 'form-control'} attrs={'cols': 24, 'rows': 10}
        }


class AvailableCarsForm(forms.ModelForm):
    model = AvailableCars
    fields = ['auto_image_field', 'auto_image_field', 'auto_description_field',
              'auto_contacts_field', 'auto_brand_title_field', 'auto_model_title_field', 'auto_link_field',
              'auto_release_date_field', 'transmission_field', 'auto_type', 'fuel_type_field',
              'eng_vol_field', 'auto_mileage_field', 'auto_VIN_vehicle', 'auto_price_BYN_field',
              'auto_price_USD_field', 'auto_location_field', 'time_create', 'time_update']
    widgets = {
        'auto_brand_title_field': forms.TextInput,
    }
# class ContactWithUsForm(forms.Form):
#     name_field = models.CharField('Имя пользователя', max_length=50)
#     email_field = models.CharField('Email пользователя', max_length=50)
#     content_field = models.TextField('Текст заданного вопроса', max_length=1000)


class AvailableMotoForm(forms.ModelForm):
    model = AvailableMoto
    fields = ['moto_image_field', 'moto_description_field', 'moto_contacts_field',
              'moto_brand_title_field', 'moto_model_title_field', 'moto_link_field',
              'moto_release_date_field', 'transmission_field', 'type_of_moto', 'fuel_type_field',
              'eng_vol_field', 'moto_mileage_field', 'moto_VIN_vehicle', 'moto_price_BYN_field',
              'moto_price_USD_field', 'moto_location_field', 'time_create', 'time_update']
    widgets = {
        'moto_brand_title_field': forms.TextInput,
    }
