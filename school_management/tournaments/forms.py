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

    def clean(self):
        bfo = self.cleaned_data.get('battle_first_oponent')
        bso = self.cleaned_data.get('battle_second_oponent')

        if bfo and bso:
            if bfo not in Classes.objects.select_related('classes'):
                raise forms.ValidationError("This class is not in tournament")
            if bso not in Classes.objects.select_related('classes'):
                raise forms.ValidationError("This class is not in tournament")
        
        return self.cleaned_data
