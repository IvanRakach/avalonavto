from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordResetView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from main.forms import ContactWithUsForm
from main.models import ContactWithUs
from .forms import *  # RegisterUserForm, LoginUSerForm
from .models import *


header_phones = [
    "+375 (17) 111-22-33",
    "+375 (33) 111-22-33",
]


def private_room_home(request):
    if request.method == 'POST':  # пользователь нажал на кнопку добавить коммент
        contact_with_us_form = ContactWithUsForm(request.POST)  # в этом объекте находятся данные, которые мы получили от пользователя из формы
        if contact_with_us_form.is_valid():  # проверяем эти данные (пользователя) на корректность заполнения
            contact_with_us_form.save()  # сохраняем данные, если они корректно заполнены
            return redirect('home')
    else:
        contact_with_us_form = ContactWithUsForm()

    moto_import_order_for_legal_persons = \
        MotorcycleOrder.objects.order_by('-moto_time_create').filter(user=request.user) \
            .filter(categories_of_customers_id=1)
    moto_import_order_for_legal_entities = \
        MotorcycleOrder.objects.order_by('-moto_time_create').filter(user=request.user) \
            .filter(categories_of_customers_id=2)
    moto_import_order_for_individual_entrepreneur = \
        MotorcycleOrder.objects.order_by('-moto_time_create').filter(user=request.user) \
            .filter(categories_of_customers_id=3)

    auto_import_order_for_legal_persons = \
        AutoOrder.objects.order_by('-auto_time_create').filter(user=request.user) \
            .filter(categories_of_customers_id=1)
    auto_import_order_for_legal_entities = \
        AutoOrder.objects.order_by('-auto_time_create').filter(user=request.user) \
            .filter(categories_of_customers_id=2)
    auto_import_order_for_individual_entrepreneur = \
        AutoOrder.objects.order_by('-auto_time_create').filter(user=request.user) \
            .filter(categories_of_customers_id=3)

    moto_service_order_for_legal_persons = \
        ServiceOrderMoto.objects.order_by('-moto_time_create').filter(user=request.user) \
            .filter(categories_of_customers_id=1)
    moto_service_order_for_legal_entities = \
        ServiceOrderMoto.objects.order_by('-moto_time_create').filter(user=request.user) \
            .filter(categories_of_customers_id=2)
    moto_service_order_for_individual_entrepreneur = \
        ServiceOrderMoto.objects.order_by('-moto_time_create').filter(user=request.user) \
            .filter(categories_of_customers_id=3)

    auto_service_order_for_legal_persons = \
        ServiceOrderAuto.objects.order_by('-auto_time_create').filter(user=request.user) \
            .filter(categories_of_customers_id=1)
    auto_service_order_for_legal_entities = \
        ServiceOrderAuto.objects.order_by('-auto_time_create').filter(user=request.user) \
            .filter(categories_of_customers_id=2)
    auto_service_order_for_individual_entrepreneur = \
        ServiceOrderAuto.objects.order_by('-auto_time_create').filter(user=request.user) \
            .filter(categories_of_customers_id=3)

    moto_safekeeping_order_for_legal_persons = \
        MotoSafekeeping.objects.order_by('-moto_time_create').filter(user=request.user) \
            .filter(categories_of_customers_id=1)
    moto_safekeeping_order_for_legal_entities = \
        MotoSafekeeping.objects.order_by('-moto_time_create').filter(user=request.user) \
            .filter(categories_of_customers_id=2)
    moto_safekeeping_order_for_individual_entrepreneur = \
        MotoSafekeeping.objects.order_by('-moto_time_create').filter(user=request.user) \
            .filter(categories_of_customers_id=3)
    # order_by('-moto_time_create')[:3] | .filter(is_published=True)

    param_for_render = {
        'moto_import_order_for_legal_persons': moto_import_order_for_legal_persons,
        'moto_import_order_for_legal_entities': moto_import_order_for_legal_entities,
        'moto_import_order_for_individual_entrepreneur': moto_import_order_for_individual_entrepreneur,

        'auto_import_order_for_legal_persons': auto_import_order_for_legal_persons,
        'auto_import_order_for_legal_entities': auto_import_order_for_legal_entities,
        'auto_import_order_for_individual_entrepreneur': auto_import_order_for_individual_entrepreneur,

        'moto_service_order_for_legal_persons': moto_service_order_for_legal_persons,
        'moto_service_order_for_legal_entities': moto_service_order_for_legal_entities,
        'moto_service_order_for_individual_entrepreneur': moto_service_order_for_individual_entrepreneur,

        'auto_service_order_for_legal_persons': auto_service_order_for_legal_persons,
        'auto_service_order_for_legal_entities': auto_service_order_for_legal_entities,
        'auto_service_order_for_individual_entrepreneur': auto_service_order_for_individual_entrepreneur,

        'moto_safekeeping_order_for_legal_persons': moto_safekeeping_order_for_legal_persons,
        'moto_safekeeping_order_for_legal_entities': moto_safekeeping_order_for_legal_entities,
        'moto_safekeeping_order_for_individual_entrepreneur': moto_safekeeping_order_for_individual_entrepreneur,

        'header_phones': header_phones,
        'contact_with_us_form': contact_with_us_form,
        # 'title': 'Отзывы о компании',
        # 'service_category_selected': 0,
    }
    return render(request, 'private_room/private_room_home.html', context=param_for_render)


def show_moto_import_order(request, moto_import_order_id):
    return HttpResponse(f"Отображение заказа с id = {moto_import_order_id}")

# ---------- регистрация и авторизация пользователей ---------- #


# class RegisterUser(CreateView):
#     form_class = RegisterUserForm  # убираем стандартный (UserCreationForm) и вставляем свой
#     template_name = 'private_room/register.html'
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
#         return redirect('private_room_home')


def register_user(request):
    if request.method == 'POST':  # пользователь нажал на кнопку добавить коммент
        contact_with_us_form = ContactWithUsForm(request.POST)  # в этом объекте находятся данные, которые мы получили от пользователя из формы
        if contact_with_us_form.is_valid():  # проверяем эти данные (пользователя) на корректность заполнения
            contact_with_us_form.save()  # сохраняем данные, если они корректно заполнены
            return redirect('home')
    else:
        contact_with_us_form = ContactWithUsForm()

    if request.method == 'POST':
        user_form = RegisterUserForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            if user_form.cleaned_data['password1'] == user_form.cleaned_data['password2']:
                new_user.set_password(user_form.cleaned_data['password1'])
            # Save the User object
                new_user.save()
                return redirect('home')
            # return render(request, 'private_room/register.html',
            #               {'new_user': new_user, 'header_phones': header_phones,
            #                'contact_with_us_form': contact_with_us_form,})
    else:
        user_form = RegisterUserForm()

    param_for_render = {
        'user_form': user_form,
        'header_phones': header_phones,
        'contact_with_us_form': contact_with_us_form,
    }
    return render(request, 'private_room/register.html', context=param_for_render)


def show_register_success(request):
    if request.method == 'POST':  # пользователь нажал на кнопку добавить коммент
        contact_with_us_form = ContactWithUsForm(request.POST)  # в этом объекте находятся данные, которые мы получили от пользователя из формы
        if contact_with_us_form.is_valid():  # проверяем эти данные (пользователя) на корректность заполнения
            contact_with_us_form.save()  # сохраняем данные, если они корректно заполнены
            return redirect('register_success')
    else:
        contact_with_us_form = ContactWithUsForm()

    param_for_render = {
        'header_phones': header_phones,
        'contact_with_us_form': contact_with_us_form,
    }
    return render(request, 'private_room/register_thx.html', context=param_for_render)


def login_user(request):
    if request.method == 'POST':  # пользователь нажал на кнопку добавить коммент
        contact_with_us_form = ContactWithUsForm(
            request.POST)  # в этом объекте находятся данные, которые мы получили от пользователя из формы
        if contact_with_us_form.is_valid():  # проверяем эти данные (пользователя) на корректность заполнения
            contact_with_us_form.save()  # сохраняем данные, если они корректно заполнены
            return redirect('register_success')
    else:
        contact_with_us_form = ContactWithUsForm()

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active and request.method == 'POST':
        # Правильный пароль и пользователь "активен"
        auth.login(request, user)
        # Перенаправление на "правильную" страницу
        param_for_render = {
            'header_phones': header_phones,
            'contact_with_us_form': contact_with_us_form,
        }
        return render(request, 'private_room/private_room_home.html', context=param_for_render)
    else:
        # Отображение страницы с ошибкой
        user_login_form = LoginUSerForm(request.POST)
        param_for_render = {
            'header_phones': header_phones,
            'user_login_form': user_login_form,
            'contact_with_us_form': contact_with_us_form,
        }
        return render(request, 'private_room/login.html', context=param_for_render)


# class LoginUser(LoginView):
#     form_class = LoginUSerForm  # AuthenticationForm
#     template_name = 'private_room/login.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title="Авторизация")  # get_user_context определен в Mixin
    #     return dict(list(context.items()) + list(c_def.items()))

    # def get_success_url(self):
    #     return reverse_lazy('private_room_home')


def logout_user(request):
    logout(request)  # logout - стандартная функция django
    return redirect('login')

# ################################################################################################ #
# ################################# Customizing PasswordResetView ################################ #
# ################################################################################################ #

# from django.core.mail import send_mail, BadHeaderError
# from django.http import HttpResponse
# from django.contrib.auth.forms import PasswordResetForm
# from django.contrib.auth.models import User
# from django.template.loader import render_to_string
# from django.db.models.query_utils import Q
# from django.contrib.auth.tokens import default_token_generator
# from django.utils.encoding import force_bytes
#
# def password_reset_request(request):
#     if request.method == 'POST':  # пользователь нажал на кнопку добавить коммент
#         contact_with_us_form = ContactWithUsForm(request.POST)  # в этом объекте находятся данные, которые мы получили от пользователя из формы
#         if contact_with_us_form.is_valid():  # проверяем эти данные (пользователя) на корректность заполнения
#             contact_with_us_form.save()  # сохраняем данные, если они корректно заполнены
#             return redirect('register_success')
#     else:
#         contact_with_us_form = ContactWithUsForm()
#
#
#     if request.method == 'POST':
#         password_form = PasswordResetForm(request.POST)
#     else:
#         password_form = PasswordResetForm()
#     param_for_render = {
#         'header_phones': header_phones,
#         'contact_with_us_form': contact_with_us_form,
#
#         'password_form': password_form,
#     }
#
#     param_for_render = {
#         'header_phones': header_phones,
#         'contact_with_us_form': contact_with_us_form,
#     }
#     return render(request, 'private_room/password_reset_form.html', context=param_for_render)


