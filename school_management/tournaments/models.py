from django.db import models
from points.models import Classes

class Tournament(models.Model):
    tournament_name = models.CharField(max_length=100)
    tournament_classes = models.ManyToManyField(Classes, null=False, related_name='classes')
    tournament_start_date = models.DateField()
    tournament_end_date = models.DateField()
    tournament_is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.tournament_name}"

class TournamentDay(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=False)
    day_date = models.DateField() 

    def __str__(self) -> str:
        return f"{self.tournament} - {self.day_date}"


class TournamentBattle(models.Model):
    WINNER_CHOICES = [
        ("FT", "First team"),
        ("ST", "Second team")
    ]

    battle_day = models.ForeignKey(TournamentDay, on_delete=models.CASCADE, null=False)
    battle_first_oponent = models.ForeignKey(Classes, on_delete=models.CASCADE, null=False, related_name="first_oponent")
    battle_second_oponent = models.ForeignKey(Classes, on_delete=models.CASCADE, null=False, related_name="second_oponent")
    battle_time = models.TimeField()
    battle_is_finished = models.BooleanField(default=False)
    winner = models.TextField(max_length=15, choices=WINNER_CHOICES, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.battle_day} - {self.battle_time} - Finished: {self.battle_is_finished}"
    