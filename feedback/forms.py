from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput
from django import forms
# ModelForm - на основе этого класса мы создадим свой собственный класс
from .models import *


class AddFeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['feedback_category'].empty_label = "Выберите категорию оказанных услуг"

    class Meta:
        model = Feedback
        # fields = '__all__'  # какие поля нужно отобразить в форме (кроме тех, заполняются автоматически)
        fields = ['author_name', 'agreement_number',  'feedback_category', 'author_photo', 'content']

        widgets = {
            'author_name': forms.TextInput(attrs={
                'class': 'form-feedback-styles',
                'placeholder': "Имя автора комментария"
            }),
            'agreement_number': forms.TextInput(attrs={
                'class': 'form-feedback-styles',
                'placeholder': "Номер договора"
            }),
            # 'feedback_category': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': "Номер договора"
            # }),
            # 'author_photo': forms.TextInput(attrs={
            #     # 'class': 'form-control',
            #     'placeholder': "Фото"
            # }),
            'content': forms.Textarea(attrs={
                'class': 'form-feedback-styles-content',
                # 'style': '''display: block;
                #  max-width: 480px;
                #   border: 1px solid lightgrey;
                #    border-radius: 4px;
                #     padding-left: 2%;
                #      padding-top: 1%;''',
                'cols': 60,
                'rows': 10,
                'placeholder': "Текст отзыва",
            })
        }

    # def clean_author_name(self):
    #     author_name = self.cleaned_data('author_name')
    #     if len(author_name) > 200:
    #         raise ValidationError('Длина превышает 200 символов')
    #     return author_name
