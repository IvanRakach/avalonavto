from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
# from django.db import models

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, FormView

from main.forms import ContactWithUsForm
from main.models import ContactWithUs

from main.utils import AvalonHomeForm
from .forms import *
from .models import *
from private_room.models import *


header_phones = [
    "+375 (17) 111-22-33",
    "+375 (29) 319-01-19",
    "+375 (33) 111-22-33",
]

# class FeedbackHome(ListView):
#     model = Feedback  # выбираем все записи из таблицы и пытается отобразить в виде списка
#     template_name = 'feedback/feedback_home.html'
#     # context_object_name = ''
#     paginate_by = 3
#
#
#     def get_queryset(self):
#         return Feedback.objects.order_by('-time_create')


def feedback_home(request):
    """Главная страница новостей + Форма из layout: свяжитесь с нами"""
    contact_list = Feedback.objects.order_by('-time_create')  # список отображаемого на странице
    paginator = Paginator(contact_list, 3)  # создаем ЭК пагинатор + количество выводимых объектов

    page_number = request.GET.get('page')  # получаем номер текущей страницы (которая отображается) с помощью GET запроса
    page_obj = paginator.get_page(page_number)  # объект - список элементов текущей страницы

    # ---------------------------------------------------------------------------------------------- #
    if request.method == 'POST':  # пользователь нажал на кнопку добавить коммент
        contact_with_us_form = ContactWithUsForm(request.POST)  # в этом объекте находятся данные, которые мы получили от пользователя из формы
        if contact_with_us_form.is_valid():  # проверяем эти данные (пользователя) на корректность заполнения
            contact_with_us_form.save()  # сохраняем данные, если они корректно заполнены
            return redirect('home')
    else:
        contact_with_us_form = ContactWithUsForm()

    feedback = Feedback.objects.order_by('-time_create')  # [:2]
    service_cats = ServiceCategory.objects.all()
    param_for_render = {
        'feedback': feedback,
        'header_phones': header_phones,
        'title': 'Отзывы о компании',
        'service_cats': service_cats,
        'service_category_selected': 0,  # 0
        'contact_with_us_form': contact_with_us_form,
        'page_obj': page_obj,
    }
    return render(request, 'feedback/feedback_home.html', context=param_for_render)


def feedback_add_by_customer(request):
    """Форма: оставтье отзыв + Форма из layout: свяжитесь с нами"""
    if request.method == 'POST':  # пользователь нажал на кнопку добавить коммент
        adding_feedback_form = AddFeedbackForm(request.POST, request.FILES)  # в этом объекте находятся данные, которые мы получили от пользователя из формы
        if adding_feedback_form.is_valid():  # проверяем эти данные (пользователя) на корректность заполнения
            adding_feedback_form.save()  # сохраняем данные, если они корректно заполнены
            return redirect('feedback_home')
    else:
        adding_feedback_form = AddFeedbackForm()

    if request.method == 'POST':  # пользователь нажал на кнопку добавить коммент
        contact_with_us_form = ContactWithUsForm(request.POST)  # в этом объекте находятся данные, которые мы получили от пользователя из формы
        if contact_with_us_form.is_valid():  # проверяем эти данные (пользователя) на корректность заполнения
            contact_with_us_form.save()  # сохраняем данные, если они корректно заполнены
            return redirect('home')
    else:
        contact_with_us_form = ContactWithUsForm()

    # adding_feedback_form = AddFeedbackForm()
    param_for_render = {
        'adding_feedback_form': adding_feedback_form,
        'header_phones': header_phones,
        'contact_with_us_form': contact_with_us_form,
    }
    return render(request, 'feedback/feedback_add_by_customer.html', context=param_for_render)


def show_fulltext_feedback(request, feedback_add_by_customer_id):
    """Отоброжение полного текста комментария оставленного пользователем + Форма из layout: свяжитесь с нами"""
    if request.method == 'POST':  # пользователь нажал на кнопку добавить коммент
        contact_with_us_form = ContactWithUsForm(request.POST)  # в этом объекте находятся данные, которые мы получили от пользователя из формы
        if contact_with_us_form.is_valid():  # проверяем эти данные (пользователя) на корректность заполнения
            contact_with_us_form.save()  # сохраняем данные, если они корректно заполнены
            return redirect('home')
    else:
        contact_with_us_form = ContactWithUsForm()

    feedback_header = get_object_or_404(Feedback, pk=feedback_add_by_customer_id)

    param_for_render = {
        'header_phones': header_phones,
        'feedback_header': feedback_header,
        'cat_selected': feedback_header.feedback_category_id,
        'contact_with_us_form': contact_with_us_form,
    }
    return render(request, 'feedback/feedbackdetails_view.html', context=param_for_render)


def show_category(request, feedback_category_id):
    """Фильтр комментариев по категориям на странице новостей + Форма из layout: свяжитесь с нами"""

    # подгрузим несколько наборов данных
    all_feedback = Feedback.objects.filter(feedback_category_id=feedback_category_id)
    # auto_feedback = Feedback.objects.filter(feedback_category_id=1).order_by('-time_create')


    # создадим объект пагинатор для всех записей из таблицы feedback
    paginator_all = Paginator(all_feedback, 3)  # создаем ЭК пагинатор + количество выводимых объектов
    page_number_all = request.GET.get('page')  # получаем номер текущей страницы (которая отображается) с помощью GET запроса
    page_obj_all_feedback = paginator_all.get_page(page_number_all)  # объект - список элементов текущей страницы
    # создадим объект пагинатор для авто
    # paginator_auto = Paginator(auto_feedback, 3)  # создаем ЭК пагинатор + количество выводимых объектов
    # page_number_auto = request.GET.get('page')  # получаем номер текущей страницы (которая отображается) с помощью GET запроса
    # page_obj_auto = paginator_auto.get_page(page_number_auto)  # объект - список элементов текущей страницы

    # -------------------------------------------------------------------------------------------------------------- #
    contact_list = Feedback.objects.order_by('-time_create')  # список отображаемого на странице
    paginator = Paginator(contact_list, 3)  # создаем ЭК пагинатор + количество выводимых объектов

    page_number = request.GET.get('page')  # получаем номер текущей страницы (которая отображается) с помощью GET запроса
    page_obj = paginator.get_page(page_number)  # объект - список элементов текущей страницы

    # -------------------------------------------------------------------------------------------------------------- #
    if request.method == 'POST':  # пользователь нажал на кнопку добавить коммент
        contact_with_us_form = ContactWithUsForm(request.POST)  # в этом объекте находятся данные, которые мы получили от пользователя из формы
        if contact_with_us_form.is_valid():  # проверяем эти данные (пользователя) на корректность заполнения
            contact_with_us_form.save()  # сохраняем данные, если они корректно заполнены
            return redirect('home')
    else:
        contact_with_us_form = ContactWithUsForm()

    feedback = Feedback.objects.filter(feedback_category_id=feedback_category_id)
    service_cats = ServiceCategory.objects.all()

    # if len(feedback) == 0:
    #     raise Http404()
    param_for_render = {
        'feedback': feedback,
        'title': 'Отзывы о компании по категориям',
        'service_cats': service_cats,
        'service_category_selected': feedback_category_id,
        'header_phones': header_phones,
        'contact_with_us_form': contact_with_us_form,
        'page_obj': page_obj,
        # ------------------------------------------------------ #
        # 'auto_feedback': auto_feedback,
        'page_obj_all_feedback': page_obj_all_feedback,
    }
    return render(request, 'feedback/feedback_home.html', context=param_for_render)

# ------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------- #


# class FeedbackUpdateView(AvalonHomeForm, UpdateView):
#     model = Feedback
#     template_name = 'feedback/feedback_add_by_customer.html'
#     form_class = AddFeedbackForm
#     success_url = 'feedback_home'
#     context_object_name = 'adding_feedback_form'

# ---------------------------------------------------------------------------------------------------- #
# вариант 1
def update_feedback(request, feedback_add_by_customer_id):

    if request.method == 'POST':  # пользователь нажал на кнопку добавить коммент
        contact_with_us_form = ContactWithUsForm(request.POST)  # в этом объекте находятся данные, которые мы получили от пользователя из формы
        if contact_with_us_form.is_valid():  # проверяем эти данные (пользователя) на корректность заполнения
            contact_with_us_form.save()  # сохраняем данные, если они корректно заполнены
            return redirect('home')
    else:
        contact_with_us_form = ContactWithUsForm()

    get_feedback = get_object_or_404(Feedback, pk=feedback_add_by_customer_id)
    if request.method == 'POST':
        adding_feedback_form = AddFeedbackForm(request.POST, request.FILES, instance=get_feedback)
        if adding_feedback_form.is_valid():
            adding_feedback_form.save()
            return redirect('feedback_home')

    param_for_render = {
        'header_phones': header_phones,
        'get_feedback': get_feedback,
        'update_feedback': True,
        'adding_feedback_form': AddFeedbackForm(instance=get_feedback),
        'contact_with_us_form': contact_with_us_form,
    }
    return render(request, 'feedback/feedback_add_by_customer.html', context=param_for_render)

# вариант 2
# def update_feedback(request, feedback_add_by_customer_id):
#     feedback = Feedback.objects.all()
#     adding_feedback_form = get_object_or_404(Feedback, pk=feedback_add_by_customer_id)
#     if request.method == "POST":
#         form = AddFeedbackForm(request.POST, instance=adding_feedback_form)
#         if form.is_valid():
#             adding_feedback_form = adding_feedback_form.save(commit=False)
#             adding_feedback_form.save()
#             #return redirect('feedback_home')
#     else:
#         adding_feedback_form = AddFeedbackForm(instance=adding_feedback_form)
#     return render(request, 'feedback/feedback_add_by_customer.html', {'adding_feedback_form': adding_feedback_form})

# вариант 3
# def update_feedback(request, feedback_add_by_customer_id):
#     try:
#         adding_feedback_form = get_object_or_404(Feedback, pk=feedback_add_by_customer_id)
#         if request.method == 'POST':
#             adding_feedback_form = AddFeedbackForm(request.POST, request.FILES)
#             adding_feedback_form.author_name = request.POST.get('author_name')
#             adding_feedback_form.agreement_number = request.POST.get('agreement_number')
#             adding_feedback_form.feedback_category = request.POST.get('feedback_category')
#             adding_feedback_form.author_photo = request.POST.get('author_photo')
#             adding_feedback_form.content = request.POST.get('content')
#             adding_feedback_form.save()
#
#             return redirect('feedback_home')
#         else:
#             param_for_render = {
#                 # 'feedback_header': feedback_header,
#                 'header_phones': header_phones,
#                 'adding_feedback_form': adding_feedback_form,
#             }
#             return render(request, "feedback/feedback_add_by_customer.html", context=param_for_render)
#     except:
#         return HttpResponseNotFound("<h2>Feedback not found</h2>")

##############
# вариант 4
# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()
#
#     return render(request, 'name.html', {'form': form})
# ---------------------------------------------------------------------------------------------------- #

class FeedbackDeleteView(AvalonHomeForm, DeleteView):
    model = Feedback
    success_url = '/feedback/'
    template_name = 'feedback/feedback_delete.html'
