from django.urls import path
from dgt import views

urlpatterns = [
    path("", views.test_index, name="test-index"),
    path("info", views.app_info, name="app-info"),
    path("<int:id>", views.question_detail, name="question-detail"),
    path("<int:id>/check/", views.check_question, name="question-check"),
]
