from django import forms
from .models import Tournament, TournamentDay, TournamentBattle, Classes


class TournamentCreateEditForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = "__all__"


class TournamentDayCreateEditForm(forms.ModelForm):
    class Meta:
        model = TournamentDay
        fields = "__all__"


class TournamentBattleCreateEditForm(forms.ModelForm):
    class Meta:
        model = TournamentBattle
        fields = ['battle_day', 'battle_first_oponent', 'battle_second_oponent', 'battle_time', 'battle_is_finished', 'winner']

    def __init__(self, *args, **kwargs):
        tournamentday_pk = kwargs.pop('tournamentday_pk')
        tournament = kwargs.pop('tournament')
        super().__init__(*args, **kwargs)
        self.fields['battle_day'].widget = forms.HiddenInput()
        self.fields['battle_day'].initial = tournamentday_pk
        self.fields['battle_first_oponent'].queryset = tournament.tournament_classes.all()
        self.fields['battle_second_oponent'].queryset = tournament.tournament_classes.all()

