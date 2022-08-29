from django.db import models

# Create your models here.

class Match(models.Model):
    match_id = models.BigIntegerField()
    lobby_id = models.BigIntegerField(null=True)
    match_uuid = models.CharField(max_length=160)
    version = models.CharField(max_length=160, null=True)
    name = models.CharField(max_length=160, null=True)
    num_players = models.IntegerField()
    num_slots = models.IntegerField()
    average_rating = models.IntegerField(null=True)
    cheats = models.BooleanField(default=False, null=True)
    full_tech_tree = models.BooleanField(default=False, null=True)
    ending_age = models.IntegerField(null=True)
    expansion = models.CharField(max_length=160, null=True)
    game_type = models.IntegerField(null=True)
    has_custom_content = models.BooleanField(null=True)
    has_password = models.BooleanField(null=True)
    lock_speed = models.BooleanField(default=True, null=True)
    lock_teams = models.BooleanField(default=True, null=True)
    map_size = models.IntegerField()
    map = models.CharField(max_length=160, null=True)
    map_id = models.IntegerField()
    population = models.IntegerField(null=True)
    ranked = models.BooleanField(null=True)
    leaderboard_id = models.IntegerField()
    rating_type = models.IntegerField()
    resources = models.IntegerField(null=True)
    # I have no idea what rms is.
    rms = models.CharField(max_length=160, null=True)
    scenario = models.CharField(max_length=160, null=True)
    server = models.CharField(max_length=160, null=True)
    shared_exploration = models.BooleanField(default=False, null=True)
    speed = models.IntegerField(null=True)
    starting_age = models.IntegerField(null=True)
    team_together = models.BooleanField(default=True, null=True)
    team_positions = models.BooleanField(default=True, null=True)
    treaty_length = models.IntegerField(null=True)
    turbo = models.BooleanField(default=False, null=True)
    victory = models.IntegerField(null=True)
    victory_time = models.IntegerField(null=True)
    visibility = models.IntegerField(null=True)
    # 'opened' is when the game lobby opened up.
    opened = models.BigIntegerField(null=True)
    started = models.BigIntegerField(null=True)
    finished = models.BigIntegerField(null=True)

class Player(models.Model):
    profile_id = models.BigIntegerField(null=False, unique=True)

class PlayerMatchStat(models.Model):
    # I added the "civ" model because it's just so unintuitive to
    # search civilizations by ids and not by name.
    civ = models.CharField(max_length=160)
    civ_id = models.IntegerField()
    profile_id = models.BigIntegerField(null=True)
    steam_id = models.BigIntegerField(null=True)
    name = models.CharField(max_length=160, null=True)
    clan = models.CharField(max_length=160, null=True)
    country = models.CharField(max_length=160, null=True)
    slot = models.IntegerField(null=True)
    slot_type = models.IntegerField(null=True)
    rating = models.IntegerField(null=True)
    rating_change = models.IntegerField(null=True)
    games = models.IntegerField(null=True)
    wins = models.IntegerField(null=True)
    streak = models.IntegerField(null=True)
    drops = models.IntegerField(null=True)
    color = models.IntegerField(null=True)
    team = models.IntegerField(null=True)
    civ_alpha_id = models.IntegerField(null=True)
    won = models.BooleanField(null=True)
    # Relevant for helping me understand Many-to-One relationships:
    # https://stackoverflow.com/questions/6928692/how-to-express-a-one-to-many-relationship-in-django
    # Further note - the related names might be confusing, but it's in the style of "Match.players"
    # or "Player.matches"
    match = models.ForeignKey(Match, related_name="players", on_delete=models.CASCADE)
    player = models.ForeignKey(Player, related_name="matches", on_delete=models.PROTECT)



