from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_home, name="feedback_home"),
    path('feedback_add_by_customer', views.feedback_add_by_customer, name="feedback_add_by_customer"),
    path('<int:feedback_add_by_customer_id>', views.show_fulltext_feedback, name='feedback-detail'),

    # path('<slug:feedback_add_by_customer_slug>/', views.FeedbackDetailsView.as_view(),
    #      name='feedback-detail'),  # show_post

    path('service_category/<int:feedback_category_id>', views.show_category, name='service_category'),  # show_category
    # path('servicecategory/<slug:feedback_category_slug>', FeedbackCategory.as_view(), name='servicecategory'),  # show_category

    # ------------------------------------------------------------------------- #
    # path('<int:pk>/update', views.FeedbackUpdateView.as_view(), name='feedback-update'),
    path('<int:feedback_add_by_customer_id>/update', views.update_feedback, name='feedback-update'),
    path('<int:pk>/delete', views.FeedbackDeleteView.as_view(),
         name='feedback-delete')
    # ------------------------------------------------------------------------- #
]
# path('', views.FeedbackHome.as_view(), name="feedback_home"),
# path('feedback/<slug:cat>/', categories),


# path('servicecategory/<int:feedback_category_id>', views.show_category, name='servicecategory'),  # show_category
