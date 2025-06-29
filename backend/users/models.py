from django.db import models
from django.contrib.auth.models import AbstractUser

# to add to the currect user class whether guest or player make roles
# first define the roles
# also add aa field rating to the user model
# do nor add a new class for user, just extend the existing User class

class User (AbstractUser):
    ROLES = (
        ('guest', 'Guest'),
        ('player', 'Player')
    )

    role = models.CharField(max_length=10, choices=ROLES, default='student')
    rating = models.FloatField(default=0.0)

    class Meta:
        db_table = 'users'  

class Friends(models.Model):
    user = models.ForeignKey(User, related_name='friends', on_delete=models.CASCADE)
    friend = models.ForeignKey(User, related_name='friend_of', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'friends'
        unique_together = ('user', 'friend')  # Ensure no duplicate friendships
        ordering = ['created_at']  # Order by creation time
