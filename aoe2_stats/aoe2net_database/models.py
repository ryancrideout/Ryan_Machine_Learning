from django.db import models

# Create your models here.

class PlayerMatchStat(models.Model):
    # I added the "civ" model because it's just so unintuitive to
    # search civilizations by ids and not by name.
    civ = models.CharField(max_length=80)
    civ_id = models.IntegerField()
    profile_id = models.IntegerField(null=True)
    steam_id = models.IntegerField(null=True)
    name = models.CharField(max_length=80, null=True)
    clan = models.CharField(max_length=80, null=True)
    country = models.CharField(max_length=80, null=True)
    slot = models.IntegerField(null=True)
    slot_type = models.IntegerField(null=True)
    rating = models.IntegerField(null=True)
    rating_change = models.IntegerField(null=True)
    games = models.IntegerField(null=True)
    wins = models.IntegerField(null=True)
    streak = models.IntegerField(null=True)
    drops = models.IntegerField(null=True)
    color = models.IntegerField()
    team = models.IntegerField(null=True)
    civ_alpha_id = models.IntegerField(null=True)
    won = models.BooleanField()

class Match(models.Model):
    match_id = models.IntegerField()
    lobby_id = models.IntegerField(null=True)
    match_uuid = models.CharField(max_length=80)
    version = models.CharField(null=True)
    name = models.CharField(max_length=80, null=True)
    num_players = models.IntegerField()
    num_slots = models.IntegerField()
    average_rating = models.IntegerField(null=True)
    cheats = models.BooleanField(default=False)

    '''
    'full_tech_tree': False, 
    'ending_age': 5, 
    'expansion': None, 
    'game_type': 0, 
    'has_custom_content': None, 
    'has_password': None, 
    'lock_speed': True, 
    'lock_teams': True, 
    'map_size': 2, 
    'map_type': 31, 
    'pop': 200, 
    'ranked': True, 
    'leaderboard_id': 4, 
    'rating_type': 4, 
    'resources': 0, 
    'rms': None, 
    'scenario': None, 
    'server': None, 
    'shared_exploration': False, 
    'speed': 2, 
    'starting_age': 0, 
    'team_together': True, 
    'team_positions': True, 
    'treaty_length': 0, 
    'turbo': False, 
    'victory': 1, 
    'victory_time': 0, 
    'visibility': 0, 
    'opened': 1596239070, 
    'started': 1596239070, 
    'finished': 1596242350, 
    'players': [
    '''