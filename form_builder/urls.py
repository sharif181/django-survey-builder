from django.urls import path

from form_builder.views import HomeView,QuestionTypeView

urlpatterns = [
    path('', HomeView.as_view()),
    path('question-type',QuestionTypeView.as_view())
]
