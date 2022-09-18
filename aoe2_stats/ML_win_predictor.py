from aoe2netapi import AOE2NETAPI

"""
Okay what do I want to filter by?

Trying to figure out "won".

Can feed the algorithm:
Player Match Data
1) civ
2) rating
3) color

Match Data:
1) map
2) started
3) (finished - started) = length

Don't we need to compare the data against whoever is playing?
"""

"""
First order of business is to make a data frame... so we need the data from above and figure out a format for it.

This will help:
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html
"""
import pandas as pd
from aoe2net_django.wsgi import *
from aoe2net_database.models import Player, Match
from aoe2netapi import AOE2NETAPI

dataframe_dict = {
    "player_one_civ": [],
    "player_one_rating": [],
    "player_one_color": [],
    "player_one_victory": [],
    "map": [],
    "time_started": [],
    "game_length": [],
    "player_two_civ": [],
    "player_two_rating": [],
    "player_two_color": [],
    "player_two_victory": [],
}

ranked_1v1_matches = Match.objects.all().filter(game_type=0, rating_type=2) 
ranked_1v1_match_ids = [match.id for match in ranked_1v1_matches]

"""
For match in match... collect data?
"""