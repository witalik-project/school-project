from django.urls import path
from . import views

urlpatterns = [
    path("", views.TournamentsList.as_view()),
    path("create", views.CreateTournament.as_view()),
    path("edit/<int:pk>", views.EditTournament.as_view()),
    path("delete/<int:pk>", views.DeleteTournament.as_view()),
]