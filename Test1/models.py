from django.db import models

class FirstTeam(models.Model):
    name = models.CharField('Player Name', max_length=120)
    team = models.CharField('Player Team', max_length=120)
    turn = models.CharField('Player turn', max_length=120)
    rank = models.CharField('Rank',max_length=60)
    score = models.CharField('Score',max_length=60)
    sixer = models.CharField('Player Sixer',max_length=60)
    four = models.CharField('Player Four',max_length=60)
    
    
class SecondTeam(models.Model):
    name1 = models.CharField('Player Name', max_length=120)
    team1 = models.CharField('Player Team', max_length=120)
    turn1 = models.CharField('Player turn', max_length=120)
    rank1 = models.CharField('Rank',max_length=60)
    over1  = models.CharField('Over',max_length=60)
    wickets = models.CharField('Wickets',max_length=60)
    wicketname = models.CharField('Wicket Name',max_length=60)