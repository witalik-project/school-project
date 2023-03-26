from django.urls import path
from . import views

urlpatterns = [
    path("", views.TournamentsList.as_view(), name="tournaments_list"),
    path("create", views.CreateTournament.as_view(), name="create_tournament"),
    path("view/<int:pk>", views.TournamentDetailView.as_view()),
    path("edit/<int:pk>", views.EditTournament.as_view()),
    path("delete/<int:pk>", views.DeleteTournament.as_view()),
    path("day/create", views.CreateTournamentDay.as_view(), name="create_tournament_day"),
    path("day/view/<int:pk>", views.TournamentDayDetailView.as_view()),
    path("battle/create", views.TournamentBattleCreate.as_view())
]