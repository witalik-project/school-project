from django.db import models
from points.models import Classes

class Tournament(models.Model):
    tournament_name = models.CharField(max_length=100)
    tournament_classes = models.ManyToManyField(Classes, null=False)
    tournament_start_date = models.DateField()
    tournament_end_date = models.DateField()
    tournament_is_active = models.BooleanField(default=False)
    
