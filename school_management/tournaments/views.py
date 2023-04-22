from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tournament, TournamentDay, TournamentBattle
from .forms import TournamentCreateEditForm, TournamentDayCreateEditForm, TournamentBattleCreateEditForm


class TournamentsList(ListView):
    template_name = "home.html"
    model = Tournament
    context_object_name = "tournaments" 


class CreateTournament(LoginRequiredMixin, CreateView):
    template_name = "create_tournament.html"
    model = Tournament
    form_class = TournamentCreateEditForm
    success_url = "/tournaments/"


class TournamentDetailView(DetailView):
    template_name = "view_tournament.html"
    model = Tournament


class EditTournament(LoginRequiredMixin, UpdateView):
    template_name = "edit_tournament.html"
    model = Tournament
    form_class = TournamentCreateEditForm
    success_url = "/tournaments/"


class DeleteTournament(LoginRequiredMixin, DeleteView):
    template_name = "delete_tournament.html"
    model = Tournament
    success_url = "/tournaments/"


class CreateTournamentDay(LoginRequiredMixin, CreateView):
    template_name = "create_day.html"
    model = TournamentDay
    form_class = TournamentDayCreateEditForm
    success_url = "/tournaments/"


class TournamentDayDetailView(DetailView):
    template_name = "view_day.html"
    model = TournamentDay


class TournamentBattleCreateView(LoginRequiredMixin ,CreateView):
    model = TournamentBattle
    form_class = TournamentBattleCreateEditForm
    template_name = 'create_battle.html'
    success_url = "/tournaments/"

    def get_context_data(self, **kwargs):
        context = super(TournamentBattleCreateView, self).get_context_data(**kwargs)
        tournamentday = get_object_or_404(TournamentDay, pk=self.kwargs['pk'])
        context['tournamentday'] = tournamentday
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        tournamentday = get_object_or_404(TournamentDay, pk=self.kwargs['pk'])
        kwargs['tournament'] = tournamentday.tournament
        kwargs['tournamentday_pk'] = self.kwargs['pk']
        return kwargs
