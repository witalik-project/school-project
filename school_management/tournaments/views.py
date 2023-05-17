from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tournament, TournamentDay, TournamentBattle
from .forms import TournamentCreateEditForm, TournamentDayCreateEditForm, TournamentBattleCreateForm, TournamentBattleEditForm, TournamentDayEditForm


class TournamentsList(ListView):
    template_name = "home.html"
    model = Tournament
    context_object_name = "tournaments" 


class CreateTournament(LoginRequiredMixin, CreateView):
    template_name = "create/create_tournament.html"
    model = Tournament
    form_class = TournamentCreateEditForm
    success_url = "/tournaments/"

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context['errors'] = form.errors
        return self.render_to_response(context=context)

class TournamentDetailView(DetailView):
    template_name = "view/view_tournament.html"
    model = Tournament


class EditTournament(LoginRequiredMixin, UpdateView):
    template_name = "edit/edit_tournament.html"
    model = Tournament
    form_class = TournamentCreateEditForm
    success_url = "/tournaments/"


class DeleteTournament(LoginRequiredMixin, DeleteView):
    template_name = "delete/delete_tournament.html"
    model = Tournament
    success_url = "/tournaments/"


class CreateTournamentDay(LoginRequiredMixin, CreateView):
    template_name = "create/create_day.html"
    model = TournamentDay
    form_class = TournamentDayCreateEditForm

    def get_success_url(self):
        return reverse_lazy('tournaments:tournament_detail', args=[self.object.tournament.pk])

    def get_context_data(self, **kwargs):
        context = super(CreateTournamentDay, self).get_context_data(**kwargs)
        tournament = get_object_or_404(Tournament, pk=self.kwargs['pk'])
        context['tournament'] = tournament
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['tournament_pk'] = self.kwargs['pk']
        return kwargs


class TournamentDayDetailView(DetailView):
    template_name = "view/view_day.html"
    model = TournamentDay


class TournamentDayEditView(LoginRequiredMixin, UpdateView):
    template_name = "edit/edit_day.html"
    model = TournamentDay
    form_class = TournamentDayEditForm

    def get_success_url(self):
        return reverse_lazy('tournaments:tournament_detail', args=[self.object.tournament.pk])
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['tournament_pk'] = self.kwargs['pk']
        return kwargs


class DeleteDay(LoginRequiredMixin, DeleteView):
    template_name = "delete/delete_day.html"
    model = TournamentDay
    
    def get_success_url(self):
        return reverse_lazy('tournaments:tournament_detail', args=[self.object.tournament.pk])


class TournamentBattleCreateView(LoginRequiredMixin, CreateView):
    template_name = "create/create_battle.html"
    model = TournamentBattle
    form_class = TournamentBattleCreateForm

    def get_success_url(self):
        return reverse_lazy('tournaments:tournament_day_detail', args=[self.object.battle_day.pk])

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
    

class TournamentBattleEditView(LoginRequiredMixin, UpdateView):
    template_name = "edit/edit_battle.html"
    model = TournamentBattle
    form_class = TournamentBattleEditForm

    def get_success_url(self):
        return reverse_lazy('tournaments:tournament_day_detail', args=[self.object.battle_day.pk])


class DeleteTournamentBattle(LoginRequiredMixin, DeleteView):
    template_name = "delete/delete_battle.html"
    model = TournamentBattle

    def get_success_url(self):
        return reverse_lazy('tournaments:tournament_day_detail', args=[self.object.battle_day.pk])
