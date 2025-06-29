from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class GameSession(models.Model):
    id = models.AutoField(primary_key=True)
    player1 = models.ForeignKey('users.User', related_name = 'player1_sessions', on_delete=models.CASCADE)
    player2 = models.ForeignKey('users.User', related_name = 'player2_sessions', on_delete=models.CASCADE)
    started_at = models.DatetimeField(default=timezone.now)
    finished_at = models.DatetimeField(null=True, blank=True)
    winner = models.ForeignKey('users.User', related_name = 'won_sessions', on_delete=models.SET_NULL, null=True, blank=True)
