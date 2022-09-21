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

"""
DOWNLOAD DATA HERE!

https://www.reddit.com/r/aoe2/comments/xj815r/aoepulse_database_dump_100_gb_5_million_games/
https://github.com/SiegeEngineers/aoe2techtree
https://archive.org/details/aoepulse_db

Guy responsible for all of this:
https://www.reddit.com/user/dj0wns/

"""
import pandas as pd
from aoe2net_django.wsgi import *
from aoe2net_database.models import Match
from aoe2netapi import AOE2NETAPI
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

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

# Make the dataframe. We're going to split this up into X and Y components.
dataframe = pd.DataFrame.from_dict(dataframe_dict)

X = dataframe.drop(columns=["player_one_victory"])
Y = dataframe["player_one_victory"]

# Make our model and our training data.
model = DecisionTreeClassifier()
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
model.fit(X_train, Y_train)
predictions = model.predict(X_test)

score = accuracy_score(Y_test, predictions)
# Be sure to print out the score!

# I think once we have the predictions (and have trained the model), then we can put it into a decision tree
# 
"""
Once we have the data we machine learn it?
"""
"""
from sklearn import tree

tree.export_graphviz(
    model, 
    out_file='music-recommender.dot', 
    feature_names=['age', 'gender'],
    class_names=sorted(Y.unique()),
    label='all',
    rounded=True,
    filled=True
)
"""