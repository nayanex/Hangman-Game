from django.db import models


class Player(models.Model):
    username = models.CharField(max_length=20, null=False, unique=True)
    lost_games = models.IntegerField(null=True)
    won_games = models.IntegerField(null=True)
    high_score = models.IntegerField(null=True)

    def __str__(self):
        """Returns a string representation of a message."""
        return f"'{self.username}' logged on  Hangman game."
