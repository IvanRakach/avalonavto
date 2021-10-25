from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView
from xml.parsers.expat import model

from feedback.forms import AddFeedbackForm
from .forms import *
from .models import *
from .forms import ContactWithUsForm
from .models import ContactWithUs
from private_room.models import *
from .utils import AvalonHomeForm

header_menu = ['Номера телефонов', 'Информация о заказанных работах и услуугах']
header_phones = [
    "+375 (17) 111-22-33",
    "+375 (33) 111-22-33",
]
# menu = [
#     {'title': "О сайте", 'url_name': 'about'},
# # ключи title - заголовок и url_name - имя маршрута к кторому будем обращаться (надо добавить в urls)
#     {'title': "Добавить статью", 'url_name': 'add_article'},
#     {'title': "Обратная связь", 'url_name': 'contact'},
#     # {'title': "Войти", 'url_name': 'login'},  # убираем, потому что написали маршру в шаблоне base html
# ]


# class AvalonHome(AvalonHomeForm, ListView):
#     template_name = 'main/index.html'
#     model = ContactWithUs
#     # context_object_name = ''  # - вывод коллекции
#     # extra_context = {'header_phones': header_phones}  # только статика
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['header_phones'] = header_phones
#         context['title'] = 'Главная страница - ООО "Авалон Авто"'
#         return context

    # публикация только тех статей, которые отмечены для публикации:
    # def get_queryset(self):
    #     return Feedback.objects.filter(is_published=True)

# ----------- логика через функцию представления ----------- #
def index(request):  # главная страница + форма обратной связи в футере
    if request.method == 'POST':  # пользователь нажал на кнопку добавить коммент
        contact_with_us_form = ContactWithUsForm(request.POST)  # в этом объекте находятся данные, которые мы получили от пользователя из формы
        if contact_with_us_form.is_valid():  # проверяем эти данные (пользователя) на корректность заполнения
            contact_with_us_form.save()  # сохраняем данные, если они корректно заполнены
            return redirect('home')
    else:
        contact_with_us_form = ContactWithUsForm()

    param_for_render = {
        'contact_with_us_form': contact_with_us_form,
        'header_phones': header_phones,
        'title': 'Главная страница - ООО "Авалон Авто"'
    }
    return render(request, 'main/index.html', context=param_for_render)


def moto_import(request):  # страница + форма обратной связи в футере
    if request.method == 'POST':  # пользователь нажал на кнопку добавить коммент
        contact_with_us_form = ContactWithUsForm(request.POST)  # в этом объекте находятся данные, которые мы получили от пользователя из формы
        if contact_with_us_form.is_valid():  # проверяем эти данные (пользователя) на корректность заполнения
            contact_with_us_form.save()  # сохраняем данные, если они корректно заполнены
            return redirect('home')
    else:
        contact_with_us_form = ContactWithUsForm()

    # вывод имеющихся для продажи мотоциклов  #
    moto_import_available_moto_offer = AvailableMoto.objects.all()
    # AvailableMoto.objects.order_by('-time_create')


    # moto_brand_filter = MotoBrand.objects.all()
    # moto_type_filter = TypeOfMotorcycleCategory.objects.all()
    # moto_engine_volume_filter = MotorcycleOrder.objects.all()
    # moto_filter = MotorcycleOrder.objects.all()

    param_for_render = {
        'moto_import_available_moto_offer': moto_import_available_moto_offer,
        'contact_with_us_form': contact_with_us_form,
        'header_phones': header_phones,
        'header_menu': header_menu,
        'title': 'Привоз мототехники - ООО "Авалон Авто"',
        'moto_filters_selected': 0,
        # 'moto_brand_filter': moto_brand_filter,
        # 'moto_type_filter': moto_type_filter,
        # 'moto_engine_volume_filter': moto_engine_volume_filter,
        # 'moto_filter': moto_filter,
    }
    return render(request, 'main/moto_import.html', context=param_for_render)


def show_moto_import_proposition(request, moto_import_available_moto_offer_slug):
    change_info(request)
    if request.method == 'POST':  # пользователь нажал на кнопку добавить коммент
        contact_with_us_form = ContactWithUsForm(
            request.POST)  # в этом объекте находятся данные, которые мы получили от пользователя из формы
        if contact_with_us_form.is_valid():  # проверяем эти данные (пользователя) на корректность заполнения
            contact_with_us_form.save()  # сохраняем данные, если они корректно заполнены
            return redirect('home')
    else:
        contact_with_us_form = ContactWithUsForm()

    moto_offer = get_object_or_404(AvailableMoto, slug=moto_import_available_moto_offer_slug)
    param_for_render = {  # это параметры для шаблона (moto_import_available_moto_offer.html)
        'moto_offer': moto_offer,
        'header_phones': header_phones,
        'contact_with_us_form': contact_with_us_form,
        # 'header_menu': header_menu,
        # 'title': 'Привоз мототехники - ООО "Авалон Авто"'
    }
    return render(request, 'main/moto_import_available_moto_offer.html', context=param_for_render)

# def show_auto_import_proposition(request, auto_import_available_auto_offer_slug):
#     auto_offer = get_object_or_404(AvailableCars, slug=auto_import_available_auto_offer_slug)
#     param_for_render = {  # это параметры для шаблона (moto_import_available_moto_offer.html)
#         'auto_offer': auto_offer,
#         'header_phones': header_phones,
#         # 'header_menu': header_menu,
#         # 'title': 'Привоз мототехники - ООО "Авалон Авто"'
#     }
#     return render(request, 'main/auto_import_available_auto_offer.html', context=param_for_render)


def auto_import(request):  # страница + форма обратной связи в футере
    if request.method == 'POST':  # пользователь нажал на кнопку добавить коммент
        contact_with_us_form = ContactWithUsForm(request.POST)  # в этом объекте находятся данные, которые мы получили от пользователя из формы
        if contact_with_us_form.is_valid():  # проверяем эти данные (пользователя) на корректность заполнения
            contact_with_us_form.save()  # сохраняем данные, если они корректно заполнены
            return redirect('home')
    else:
        contact_with_us_form = ContactWithUsForm()

    auto_import_available_auto_offer = AvailableCars.objects.all()

    params_for_render = {
        'auto_import_available_auto_offer': auto_import_available_auto_offer,
        'contact_with_us_form': contact_with_us_form,
        'header_phones': header_phones,
        'header_menu': header_menu,
        'title': 'Привоз автомобилей - ООО "Авалон Авто"'
    }
    return render(request, 'main/auto_import.html', context=params_for_render)


def show_auto_import_proposition(request, auto_import_available_auto_offer_slug):
    auto_offer = get_object_or_404(AvailableCars, slug=auto_import_available_auto_offer_slug)
    change_info(request)
    if request.method == 'POST':  # пользователь нажал на кнопку добавить коммент
        contact_with_us_form = ContactWithUsForm(
            request.POST)  # в этом объекте находятся данные, которые мы получили от пользователя из формы
        if contact_with_us_form.is_valid():  # проверяем эти данные (пользователя) на корректность заполнения
            contact_with_us_form.save()  # сохраняем данные, если они корректно заполнены
            return redirect('home')
    else:
        contact_with_us_form = ContactWithUsForm()

    param_for_render = {  # это параметры для шаблона (moto_import_available_moto_offer.html)
        'auto_offer': auto_offer,
        'header_phones': header_phones,
        'contact_with_us_form': contact_with_us_form,
        # 'header_menu': header_menu,
        # 'title': 'Привоз мототехники - ООО "Авалон Авто"'
    }
    return render(request, 'main/auto_import_available_auto_offer.html', context=param_for_render)


def moto_service(request):  # страница + форма обратной связи в футере
    if request.method == 'POST':  # пользователь нажал на кнопку добавить коммент
        contact_with_us_form = ContactWithUsForm(
            request.POST)  # в этом объекте находятся данные, которые мы получили от пользователя из формы
        if contact_with_us_form.is_valid():  # проверяем эти данные (пользователя) на корректность заполнения
            contact_with_us_form.save()  # сохраняем данные, если они корректно заполнены
            return redirect('home')
    else:
        contact_with_us_form = ContactWithUsForm()

    moto_service_services_list = MotoTypesOfServices.objects.all()

    if request.method == 'POST':
        form = ContactWithUsForm(request.POST)
        if form.is_valid():
            try:
                ContactWithUs.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, '''Ошибка отправки формы "свяжитесь с нами"''')
    else:
        form_contact_with_us = ContactWithUsForm()

    params_for_render = {
        'moto_service_services_list': moto_service_services_list,
        'contact_with_us_form': contact_with_us_form,
        'header_phones': header_phones,
        'header_menu': header_menu,
        'title': 'СТО мототехники - ООО "Авалон Авто"',
    }
    return render(request, 'main/moto_service.html', context=params_for_render)


def moto_safekeeping(request):  # страница + форма обратной связи в футере
    if request.method == 'POST':  # пользователь нажал на кнопку добавить коммент
        contact_with_us_form = ContactWithUsForm(
            request.POST)  # в этом объекте находятся данные, которые мы получили от пользователя из формы
        if contact_with_us_form.is_valid():  # проверяем эти данные (пользователя) на корректность заполнения
            contact_with_us_form.save()  # сохраняем данные, если они корректно заполнены
            return redirect('home')
    else:
        contact_with_us_form = ContactWithUsForm()

    params_for_render = {
        'contact_with_us_form': contact_with_us_form,
        'header_phones': header_phones,
        'header_menu': header_menu,
        'title': 'Мотохранение - ООО "Авалон Авто"',
    }
    return render(request, 'main/moto_safekeeping.html', context=params_for_render)


def about(request):  # страница + форма обратной связи в футере
    if request.method == 'POST':  # пользователь нажал на кнопку добавить коммент
        contact_with_us_form = ContactWithUsForm(
            request.POST)  # в этом объекте находятся данные, которые мы получили от пользователя из формы
        if contact_with_us_form.is_valid():  # проверяем эти данные (пользователя) на корректность заполнения
            contact_with_us_form.save()  # сохраняем данные, если они корректно заполнены
            return redirect('home')
    else:
        contact_with_us_form = ContactWithUsForm()

    params_for_render = {
        'contact_with_us_form': contact_with_us_form,
        'header_phones': header_phones,
        'title': 'О нас - ООО "Авалон Авто"',
    }
    return render(request, 'main/about.html', context=params_for_render)


# ##################################################################################### #

from .models import *
from django.utils import timezone

# Пользовательская функция, а не просмотр
def change_info(request):       # Модифицировать информацию, такую как посещаемость сайта и IP
    # Для каждого посещения добавьте 1 к общему количеству посещений.
    count_nums = VisitNumber.objects.filter(id=1)
    if count_nums:
        count_nums = count_nums[0]
        count_nums.count += 1
    else:
        count_nums = VisitNumber()
        count_nums.count = 1
    count_nums.save()

    # Запишите количество посещений ip и каждого ip
    if 'HTTP_X_FORWARDED_FOR' in request.META:  # Получить IP
        client_ip = request.META['HTTP_X_FORWARDED_FOR']
        client_ip = client_ip.split(",")[0]  # Так вот настоящий айпи
    else:
        client_ip = request.META['REMOTE_ADDR']  # Получить IP прокси здесь
    # print(client_ip)

    ip_exist = Userip.objects.filter(ip=str(client_ip))
    if ip_exist:  # Определить, существует ли ip
        uobj = ip_exist[0]
        uobj.count += 1
    else:
        uobj = Userip()
        uobj.ip = client_ip
        uobj.count = 1
    uobj.save()

    # Увеличение сегодняшних посещений
    date = timezone.now().date()
    today = DayNumber.objects.filter(day=date)
    if today:
        temp = today[0]
        temp.count += 1
    else:
        temp = DayNumber()
        temp.dayTime = date
        temp.count = 1
    temp.save()













# ##################################################################################### #


# ---------- форма "СВЯЖИТЕСЬ С НАМИ" в футере на главной странице (начало) ---------- #
# def _contact_with_us(request):
#     form_contact_with_us = ContactWithUsForm
#     param_for_render = {
#         'form_contact_with_us': form_contact_with_us,
#     }
#     return render(request, 'main/index.html', context=param_for_render)

# def contact_with_us(request):
#     if request.method == 'POST':
#         form = ContactWithUsForm(request.POST)
#         if form.is_valid():
#             try:
#                 ContactWithUs.objects.create(**form.cleaned_data)
#                 return redirect('home')
#
#             except:
#                 form.add_error(None, '''Ошибка отправки формы "свяжитесь с нами"''')
#
#     else:
#         form = ContactWithUsForm()
#
#     return render(request, 'main/index.html', {'form': form, })
# ---------- форма "СВЯЖИТЕСЬ С НАМИ" в футере на главной странице (конец) ---------- #

# ---------- регистрация и авторизация пользователей ---------- #

# class RegisterUser(CreateView):
#     form_class = RegisterUserForm  # убираем стандартный (UserCreationForm) и вставляем свой
#     template_name = 'main/register.html'
#     success_url = reverse_lazy('login')
#
#     # def get_context_data(self, *, object_list=None, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     c_def = self.get_user_context(title="Регистрация")  # get_user_context определен в Mixin
#     #     return dict(list(context.items()) + list(c_def.items()))  # context
#
#     # если пользователь зарегестрировался, то он будет автоматические и авторизовываться
#     def form_valid(self, form):  # form_valid - этот метод вызывается при успешной проверке формы регистарции, а значит - при успешной регистрации
#         user = form.save()  # добавляем пользователя в БД (сохраняем форму в БД)
#         login(self.request, user)  # затем, вызываем спец. функцию django (login), которая авторизовывает пользователя; user - зарегестрированный пользователь
#         return redirect('home')
#
#
# class LoginUser(LoginView):
#     form_class = LoginUSerForm  # AuthenticationForm
#     template_name = 'main/login.html'
#
#     # def get_context_data(self, *, object_list=None, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     c_def = self.get_user_context(title="Авторизация")  # get_user_context определен в Mixin
#     #     return dict(list(context.items()) + list(c_def.items()))
#
#     def get_success_url(self):
#         return reverse_lazy('home')
#
#
# def logout_user(request):
#     logout(request)  # logout - стандартная функция django
#     return redirect('login')
