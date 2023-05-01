from django import forms
from .models import Tournament, TournamentDay, TournamentBattle


class TournamentCreateEditForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = "__all__"
        labels = {
            "tournament_start_date": "Tournament start date (YYYY-MM-DD)",
            "tournament_end_date": "Tournament end date (YYYY-MM-DD)",
        }
    
    def clean(self):
        cleaned_data = super().clean()
        classes = cleaned_data.get('tournament_classes')

        if classes:
            if classes.count() < 2:
                raise forms.ValidationError("Classes in tournament need to be at least 2")

        return cleaned_data


class TournamentDayCreateEditForm(forms.ModelForm):
    class Meta:
        model = TournamentDay
        fields = "__all__"
        labels = {
            "day_date": "Day date (YYYY-MM-DD)"
        }
    
    def __init__(self, *args, **kwargs):
        tournament_pk = kwargs.pop('tournament_pk')
        super().__init__(*args, **kwargs)
        self.fields['tournament'].widget = forms.HiddenInput()
        self.fields['tournament'].initial = tournament_pk
    

class TournamentDayEditForm(forms.ModelForm):
    class Meta:
        model = TournamentDay
        fields = ['day_date']
        labels = {
            "day_date": "Day date (YYYY-MM-DD)"
        }

class TournamentBattleCreateForm(forms.ModelForm):
    class Meta:
        model = TournamentBattle
        fields = ['battle_day', 'battle_first_oponent', 'battle_second_oponent', 'battle_time', 'battle_is_finished', 'winner']
        labels = {
            "battle_time": "Battle time (hh:mm)"
        }

    def __init__(self, *args, **kwargs):
        tournamentday_pk = kwargs.pop('tournamentday_pk')
        tournament = kwargs.pop('tournament')
        super().__init__(*args, **kwargs)
        self.fields['battle_day'].widget = forms.HiddenInput()
        self.fields['battle_day'].initial = tournamentday_pk
        self.fields['battle_first_oponent'].queryset = tournament.tournament_classes.all()
        self.fields['battle_second_oponent'].queryset = tournament.tournament_classes.all()

    def clean(self):
        cleaned_data = super().clean()
        bfo = cleaned_data.get('battle_first_oponent')
        bso = cleaned_data.get('battle_second_oponent')

        if bfo and bso:
            if bfo == bso:
                raise forms.ValidationError("Oponents cannot bet the same")
        
        return cleaned_data


class TournamentBattleEditForm(forms.ModelForm):
    class Meta:
        model = TournamentBattle
        fields = ['battle_first_oponent', 'battle_second_oponent', 'battle_time', 'battle_is_finished', 'winner']
        labels = {
            "battle_time": "Battle time (hh:mm)"
        }
