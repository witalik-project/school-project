from django.contrib import admin
from . import models

admin.site.register(models.Tournament)
admin.site.register(models.TournamentDay)
admin.site.register(models.TournamentBattle)
