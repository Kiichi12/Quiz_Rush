from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from question.models import Question, Choices
from game.models import GameSession


class AnswerLog(models.Model):
    session = models.ForeignKey('game.GameSession', related_name='answer_logs', on_delete=models.CASCADE)
    question = models.ForeignKey('question.Question', related_name='answer_logs', on_delete=models.CASCADE)
    player = models.ForeignKey('users.User', related_name='answer_logs', on_delete=models.CASCADE)
    answer = models.ForeignKey('question.Choices', related_name='answer_logs', on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    answered_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'answer_logs'
        unique_together = ('session', 'question', 'player')

class PlayerScore(models.Model):
    session = models.ForeignKey('game.GameSession', related_name='player_scores', on_delete=models.CASCADE)
    player = models.ForeignKey('users.User', related_name='player_scores', on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    correct_count = models.IntegerField(default=0)
    incorrect_count = models.IntegerField(default=0)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'player_scores'
        unique_together = ('session', 'player')
