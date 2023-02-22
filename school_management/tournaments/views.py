from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, DeletionMixin
from .models import Tournament
from .forms import TournamentCreateEditForm


class TournamentsList(ListView):
    template_name = "home.html"
    model = Tournament
    context_object_name = "tournaments" 


class CreateTournament(LoginRequiredMixin, CreateView):
    template_name = "create_tournament.html"
    model = Tournament
    form_class = TournamentCreateEditForm
    success_url = "/tournaments/"


class EditTournament(LoginRequiredMixin, UpdateView):
    template_name = "edit_tournament.html"
    model = Tournament
    form_class = TournamentCreateEditForm
    success_url = "/tournaments/"


class DeleteTournament(LoginRequiredMixin, DeleteView):
    template_name = "delete_tournament.html"
    model = Tournament
    success_url = "/tournaments/"
