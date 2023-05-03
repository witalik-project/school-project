from django.db import models
from points.models import Classes

class Tournament(models.Model):
    tournament_name = models.CharField(verbose_name="Nazwa turnieju", max_length=100)
    tournament_classes = models.ManyToManyField(Classes, verbose_name="Uczestniczące klasy", null=False, related_name='classes')
    tournament_start_date = models.DateField(verbose_name="Data początku")
    tournament_end_date = models.DateField(verbose_name="Data końca")
    tournament_is_active = models.BooleanField(verbose_name="Aktywny (tak/nie)", default=False)

    def __str__(self) -> str:
        return f"{self.tournament_name}"

class TournamentDay(models.Model):
    tournament = models.ForeignKey(Tournament, verbose_name="Turniej", on_delete=models.CASCADE, null=False)
    day_date = models.DateField(verbose_name="Data") 

    def __str__(self) -> str:
        return f"{self.tournament} - {self.day_date}"


class TournamentBattle(models.Model):
    CHOICES = [
        ("FO", "Pierwszy przeciwnik"),
        ("SO", "Drugi przeciwnik")
    ]
    battle_day = models.ForeignKey(TournamentDay, verbose_name="Dzień", on_delete=models.CASCADE, null=False)
    battle_first_oponent = models.ForeignKey(Classes, verbose_name="Pierwszy przeciwnik",  on_delete=models.CASCADE, related_name="first_oponent", to_field="id")
    battle_second_oponent = models.ForeignKey(Classes, verbose_name="Drugi przeciwnik", on_delete=models.CASCADE, related_name="second_oponent", to_field="id")
    battle_time = models.TimeField(verbose_name="Czas pojedynku")
    battle_is_finished = models.BooleanField(verbose_name="Pojedynek skończony", default=False)
    winner = models.TextField(verbose_name="Zwycięzca", max_length=50, choices=CHOICES, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.battle_day} - {self.battle_time} - Finished: {self.battle_is_finished}"
