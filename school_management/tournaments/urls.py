from django.urls import path
from . import views

app_name = "tournaments"

urlpatterns = [
    path("", views.TournamentsList.as_view(), name="tournaments_list"),
    path("create", views.CreateTournament.as_view(), name="tournament_create"),
    path("view/<int:pk>", views.TournamentDetailView.as_view(), name="tournament_detail"),
    path("edit/<int:pk>", views.EditTournament.as_view(), name="tournament_edit"),
    path("delete/<int:pk>", views.DeleteTournament.as_view(), name="tournament_delete"),
    path("day/create/<int:pk>", views.CreateTournamentDay.as_view(), name="tournament_day_create"),
    path("day/view/<int:pk>", views.TournamentDayDetailView.as_view(), name="tournament_day_detail"),
    path("day/edit/<int:pk>", views.TournamentDayEditView.as_view(), name="tournament_day_edit"),
    path("day/delete/<int:pk>", views.DeleteDay.as_view(), name="tournament_day_delete"),
    path("battle/create/<int:pk>", views.TournamentBattleCreateView.as_view(), name="tournament_battle_create"),
    path("battle/edit/<int:pk>", views.TournamentBattleEditView.as_view(), name="tournament_battle_edit"),
    path("battle/delete/<int:pk>", views.DeleteTournamentBattle.as_view(), name="tournament_battle_delete")
]