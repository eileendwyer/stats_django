from django.db import models

# Create your models here.
class GoalieStats(models.Model):
    PlayerName = models.CharField(max_length=30)
    TeamName = models.CharField(max_length=30)
    GamesPlayed = models.FloatField(max_length=3)
    MinutesPlayed = models.FloatField(max_length=4)
    ShotsonGoal = models.FloatField(max_length=3)
    Saves = models.FloatField(max_length=3)
    GA = models.FloatField(max_length=3)
    GAA = models.FloatField(max_length=6)
    SHO = models.FloatField(max_length=2)


def __str__(self):
    return self.PlayerName
