from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name="home"),
    # path('', AvalonHome.as_view(), name="home"),
    path('moto_import', views.moto_import, name="moto_import"),
    path('moto_import/<slug:moto_import_available_moto_offer_slug>', show_moto_import_proposition,
         name='moto_import_available_moto_offer'),
    path('auto_import', views.auto_import, name="auto_import"),
    path('auto_import/<slug:auto_import_available_auto_offer_slug>', show_auto_import_proposition,
         name='auto_import_available_auto_offer'),
    path('moto_service', views.moto_service, name="moto_service"),
    path('moto_safekeeping', views.moto_safekeeping, name="moto_safekeeping"),
    path('about_us', views.about, name="about_us"),


    # path('moto_import/<int:moto_import_available_moto_offer_id>', show_moto_import_proposition,
    #      name='moto_import_available_moto_offer'),

    # path('login/', LoginUser.as_view(), name='login'),
    # path('logout/', logout_user, name='logout'),
    # path('register/', RegisterUser.as_view(), name='register'),

    # path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
]
