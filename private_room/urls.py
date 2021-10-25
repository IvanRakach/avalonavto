from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    path('', views.private_room_home, name="private_room_home"),
    # path('login/', LoginUser.as_view(), name='login'),
    path('login/', views.login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    # path('register/', RegisterUser.as_view(), name='register'),
    path('register/', views.register_user, name='register'),
    path('register_success/', views.show_register_success, name='register_success'),
    path('moto_import_order/<int:moto_import_order_id>', show_moto_import_order, name='moto_import_order'),


    # path('password_reset/', views.password_reset_request, name='password_reset'),

    path('password_reset/',
         PasswordResetView.as_view(
             template_name='private_room/password_reset_form.html'
         ),
         name='password_reset'),
    path('password_reset/done/',
         PasswordResetDoneView.as_view(
            template_name='private_room/password_reset_done.html',
         ),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
            template_name='private_room/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('reset/done/',
         PasswordResetCompleteView.as_view(
            template_name='private_room/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]








# urlpatterns = [
#     # path('', views.FeedbackHome.as_view(), name="feedback_home"),
#     path('', views.feedback_home, name="feedback_home"),
#     # path('feedback_add_by_customer', views.AddFeedbackOnWebSite.as_view(), name="feedback_add_by_customer"),
#     path('feedback_add_by_customer', views.feedback_add_by_customer, name="feedback_add_by_customer"),
#     path('feedback/<slug:cat>/', categories),
#     path('<int:pk>', views.FeedbackDetailsView.as_view(), name='feedback-detail'),  # show_post
#     path('servicecategory/<int:feedback_category_id>', views.show_category, name='servicecategory'),  # show_category
#     path('<int:pk>/update', views.FeedbackUpdateView.as_view(), name='feedback-update'),
#     path('<int:pk>/delete', views.FeedbackDeleteView.as_view(), name='feedback-delete')
# ]
