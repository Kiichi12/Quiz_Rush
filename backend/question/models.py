from django.db import models
from django.utils import timezone



class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_text = models.TextField()
    difficulty = models.SmallIntegerField(default=1)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'questions'
        ordering = ['difficulty', 'created_at']  # Order by difficulty and creation time

class Choices(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.TextField()
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'choices'
        unique_together = ('question', 'choice_text')  # Ensure no duplicate choices for a question