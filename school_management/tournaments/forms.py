from django import forms
from .models import Tournament


class TournamentCreateEditForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = "__all__"