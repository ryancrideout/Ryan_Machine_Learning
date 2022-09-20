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

# Don't have to do fancy footwork with splitting up the real data from
# test data, the algorithm is smart enough to do that for me.
matches_count = len(ranked_1v1_matches)

"""
For match in match... collect data?
"""
for match in ranked_1v1_matches:
    dataframe_dict["map"].append(match.map)
    dataframe_dict["time_started"].append(match.started)
    length = match.finished - match.started
    dataframe_dict["game_length"].append(length)
    player_one = match.players[0]
    player_two = match.players[1]

    # We need a color map - 1 is red, 2 is blue, etc.
    dataframe_dict["player_one_civ"].append(player_one.civ)
    dataframe_dict["player_one_rating"].append(player_one.rating)
    dataframe_dict["player_one_color"].append(player_one.color)
    # I think this will be our "Y" value.
    dataframe_dict["player_one_victory"].append(player_one.won)

    dataframe_dict["player_two_civ"].append(player_two.civ)
    dataframe_dict["player_two_rating"].append(player_two.rating)
    dataframe_dict["player_two_color"].append(player_two.color)
    dataframe_dict["player_two_victory"].append(player_two.won)

"""
Once we have the data we machine learn it?
"""
"""
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# This allocates 20% of the data for testing, the other 80% will be for training.
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
model.fit(X_train, Y_train)
predictions = model.predict(X_test)

score = accuracy_score(Y_test, predictions)
score
"""