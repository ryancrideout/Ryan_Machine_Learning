# This is the file we use to make AoE2 API calls - site: https://aoe2.net/#
import requests
import json

# response = requests.get("https://aoe2.net/api/strings?game=aoe2de&language=en") # Put this in a class somehow?
# api_strings = json.loads(response.content)

# print(api_strings.keys())
'''
dict_keys(['language', 'age', 'civ', 'game_type', 'leaderboard', 'map_size', 'map_type', 'rating_type', 'resources', 'speed', 'victory', 'visibility'])
'''

# print(api_strings['civ'])
'''
[{'id': 1, 'string': 'Britons'}, {'id': 2, 'string': 'Franks'}, {'id': 3, 'string': 'Goths'}, {'id': 4, 'string': 'Teutons'}, {'id': 5, 'string': 'Japanese'}, {'id': 6, 'string': 'Chinese'}, 
{'id': 7, 'string': 'Byzantines'}, {'id': 8, 'string': 'Persians'}, {'id': 9, 'string': 'Saracens'}, {'id': 10, 'string': 'Turks'}, {'id': 11, 'string': 'Vikings'}, {'id': 12, 'string': 'Mongols'}, 
{'id': 13, 'string': 'Celts'}, {'id': 14, 'string': 'Spanish'}, {'id': 15, 'string': 'Aztecs'}, {'id': 16, 'string': 'Mayans'}, {'id': 17, 'string': 'Huns'}, {'id': 18, 'string': 'Koreans'}, 
{'id': 19, 'string': 'Italians'}, {'id': 20, 'string': 'Hindustanis'}, {'id': 21, 'string': 'Incas'}, {'id': 22, 'string': 'Magyars'}, {'id': 23, 'string': 'Slavs'}, {'id': 24, 'string': 'Portuguese'}, 
{'id': 25, 'string': 'Ethiopians'}, {'id': 26, 'string': 'Malians'}, {'id': 27, 'string': 'Berbers'}, {'id': 28, 'string': 'Khmer'}, {'id': 29, 'string': 'Malay'}, {'id': 30, 'string': 'Burmese'}, 
{'id': 31, 'string': 'Vietnamese'}, {'id': 32, 'string': 'Bulgarians'}, {'id': 33, 'string': 'Tatars'}, {'id': 34, 'string': 'Cumans'}, {'id': 35, 'string': 'Lithuanians'}, {'id': 36, 'string': 'Burgundians'}, 
{'id': 37, 'string': 'Sicilians'}, {'id': 38, 'string': 'Poles'}, {'id': 39, 'string': 'Bohemians'}, {'id': 40, 'string': 'Dravidians'}, {'id': 41, 'string': 'Bengalis'}, {'id': 42, 'string': 'Gurjaras'}, 
{'id': 43, 'string': 'Indians'}]
'''

# print(api_strings['leaderboard'])
'''
[{'id': 0, 'string': 'Unranked'}, {'id': 1, 'string': '1v1 Death Match'}, {'id': 2, 'string': 'Team Death Match'}, {'id': 3, 'string': '1v1 Random Map'}, 
{'id': 4, 'string': 'Team Random Map'}, {'id': 13, 'string': '1v1 Empire Wars'}, {'id': 14, 'string': 'Team Empire Wars'}]
'''

# print(api_strings['rating_type'])
'''
[{'id': 0, 'string': 'Unranked'}, {'id': 1, 'string': '1v1 Death Match'}, {'id': 2, 'string': '1v1 Random Map'}, {'id': 3, 'string': 'Team Death Match'}, {'id': 4, 'string': 'Team Random Map'}, 
{'id': 5, 'string': '1v1 Random Map Quick Play'}, {'id': 6, 'string': 'Team Random Map Quick Play'}, {'id': 7, 'string': '1v1 Empire Wars Quick Play'}, {'id': 8, 'string': 'Team Empire Wars Quick Play'}, 
{'id': 9, 'string': 'Battle Royale Quick Play'}, {'id': 13, 'string': '1v1 Empire Wars'}, {'id': 14, 'string': 'Team Empire Wars'}]
'''

# response = requests.get("https://aoe2.net/api/player/lastmatch?game=aoe2de&steam_id=76561198027378107") 
# response_data = json.loads(response.content)
# print(response_data)
'''
{'profile_id': 208393, 'steam_id': '76561198027378107', 'name': 'Nicov', 'country': 'AR', 
'last_match': {'match_id': '158631992', 'lobby_id': '109775242739423949', 
'match_uuid': '2d90a316-ad62-d642-96ee-bee48c8f1644', 'version': '61591', 
'name': "Nicov's Game [RDLA_Canyon]", 'num_players': 2, 'num_slots': 2, 
'average_rating': 2604, 'cheats': False, 'full_tech_tree': False, 'ending_age': 0, 'expansion': None, 
'game_type': 0, 'has_custom_content': None, 'has_password': False, 'lock_speed': True, 'lock_teams': True, 'map_size': 0,
 'map_type': 59, 'pop': 250, 'ranked': False, 'leaderboard_id': 0, 'rating_type': 0, 'resources': 0, 'rms': 'RDLA_Canyon.rms', 'scenario': None, 'server': 'westeurope', 
 'shared_exploration': False, 'speed': 2, 'starting_age': 0, 'team_together': True, 'team_positions': False, 'treaty_length': 0, 'turbo': False, 
 'victory': 1, 'victory_time': 1, 'visibility': 0, 'opened': 1652039824, 'started': 1652039824, 'finished': None, 
 'players': [
     {'profile_id': 208393, 'steam_id': '76561198027378107', 'name': 'Nicov', 'clan': None, 'country': None, 'slot': 1, 'slot_type': 1, 'rating': 2621, 'rating_change': None, 
    'games': None, 'wins': None, 'streak': None, 'drops': None, 'color': 1, 'team': -1, 'civ': 2, 'civ_alpha': 14, 'won': None}, 
    {'profile_id': 197388, 'steam_id': '76561198088251629', 'name': 'GL.TaToH', 'clan': None, 'country': None, 'slot': 2, 'slot_type': 1, 'rating': 2587, 'rating_change': None, 
    'games': None, 'wins': None, 'streak': None, 'drops': None, 'color': 2, 'team': -1, 'civ': 16, 'civ_alpha': 28, 'won': None}]}}
'''

# response = requests.get("https://aoe2.net/api/player/matches?game=aoe2de&steam_id=76561198027378107&count=5") 
# response_data = json.loads(response.content)
# print(response_data[4])
'''
{'match_id': '158467315', 'lobby_id': None, 'match_uuid': '44dac5c8-df19-f54a-8058-d0f2b08c7134', 'version': '61591', 'name': 'AUTOMATCH', 'num_players': 4, 'num_slots': 4, 'average_rating': None, 'cheats': False, 
'full_tech_tree': False, 'ending_age': 5, 'expansion': None, 'game_type': 0, 'has_custom_content': None, 'has_password': True, 'lock_speed': True, 'lock_teams': True, 'map_size': 2, 'map_type': 140, 'pop': 200, 
'ranked': True, 'leaderboard_id': 4, 'rating_type': 4, 'resources': 1, 'rms': None, 'scenario': None, 'server': 'eastus', 'shared_exploration': False, 'speed': 2, 'starting_age': 2, 'team_together': True, 
'team_positions': True, 'treaty_length': 0, 'turbo': False, 'victory': 1, 'victory_time': 0, 'visibility': 0, 'opened': 1651970625, 'started': 1651970625, 'finished': 1651971419, 
'players': [{'profile_id': 283233, 'steam_id': '76561198091184792', 'name': 'ashleylynn', 'clan': None, 'country': 'US', 'slot': 1, 'slot_type': 1, 'rating': 2627, 'rating_change': 2, 'games': None, 'wins': None,
 'streak': None, 'drops': None, 'color': 2, 'team': 1, 'civ': 35, 'civ_alpha': 24, 'won': True}, {'profile_id': 4234652, 'steam_id': '76561198923821557', 'name': '_The_Oldergold', 'clan': None, 'country': 'PE', 
 'slot': 2, 'slot_type': 1, 'rating': 2637, 'rating_change': -2, 'games': None, 'wins': None, 'streak': None, 'drops': None, 'color': 1, 'team': 2, 'civ': 11, 'civ_alpha': 41, 'won': False}, 
 {'profile_id': 208393, 'steam_id': '76561198027378107', 'name': 'Nicov', 'clan': None, 'country': 'AR', 'slot': 3, 'slot_type': 1, 'rating': 3259, 'rating_change': 2, 'games': None, 'wins': None, 'streak': None, 
 'drops': None, 'color': 4, 'team': 1, 'civ': 15, 'civ_alpha': 0, 'won': True}, {'profile_id': 6845183, 'steam_id': '76561199213255411', 'name': 'Thomas21', 'clan': None, 'country': 'JP', 'slot': 4, 
 'slot_type': 1, 'rating': 2621, 'rating_change': -2, 'games': None, 'wins': None, 'streak': None, 'drops': None, 'color': 3, 'team': 2, 'civ': 2, 'civ_alpha': 14, 'won': False}]}
'''

# I guess we'll have to make requests since the beginning of time? Maybe just do 2021.
# response = requests.get("https://aoe2.net/api/matches?game=aoe2de&count=10&since=1570567008") 
# response_data = json.loads(response.content)
# print(response_data)

# ID - '76561198027378107'
# Timestamp - 1596238991 # July 31st, 2020?
# Timestamp - 1570567008
# Rating - Elo

# Match ID: 0d9b38e1-1042-6a4c-bf73-af3221625368
# response = requests.get("https://aoe2.net/api/match?uuid=0d9b38e1-1042-6a4c-bf73-af3221625368") 
# response_data = json.loads(response.content)
# print(response_data)
'''
{'match_id': '32236444', 'lobby_id': None, 'match_uuid': '0d9b38e1-1042-6a4c-bf73-af3221625368', 'version': None, 'name': 'équipes équilibrées', 'num_players': 6, 'num_slots': 6, 'average_rating': None, 
'cheats': False, 'full_tech_tree': False, 'ending_age': 0, 'expansion': None, 'game_type': 0, 'has_custom_content': None, 'has_password': None, 'lock_speed': True, 'lock_teams': True, 'map_size': 3, 
'map_type': 9, 'pop': 200, 'ranked': False, 'leaderboard_id': 0, 'rating_type': 0, 'resources': 0, 'rms': None, 'scenario': None, 'server': None, 'shared_exploration': False, 'speed': 2, 'starting_age': 0, 
'team_together': True, 'team_positions': True, 'treaty_length': 0, 'turbo': False, 'victory': 1, 'victory_time': 1, 'visibility': 0, 'opened': 1596229705, 'started': 1596229705, 'finished': 1596245475, 

'players': [{'profile_id': 1121013, 'steam_id': None, 'name': None, 'clan': None, 'country': None, 'slot': 1, 'slot_type': 1, 'rating': 1981, 'rating_change': None, 'games': None, 'wins': None, 'streak': None, 
'drops': None, 'color': 2, 'team': 1, 'civ': 32, 'civ_alpha': 3, 'won': False}, {'profile_id': 1536019, 'steam_id': None, 'name': None, 'clan': None, 'country': None, 'slot': 2, 'slot_type': 1, 'rating': 2022, 
'rating_change': None, 'games': None, 'wins': None, 'streak': None, 'drops': None, 'color': 4, 'team': 2, 'civ': 31, 'civ_alpha': 33, 'won': True}, {'profile_id': 1831974, 'steam_id': None, 'name': None, 
'clan': None, 'country': None, 'slot': 3, 'slot_type': 1, 'rating': 2006, 'rating_change': None, 'games': None, 'wins': None, 'streak': None, 'drops': None, 'color': 1, 'team': 1, 'civ': 18, 'civ_alpha': 18, 
'won': False}, {'profile_id': 2641034, 'steam_id': None, 'name': None, 'clan': None, 'country': None, 'slot': 4, 'slot_type': 1, 'rating': 1914, 'rating_change': None, 'games': None, 'wins': None, 'streak': None, 
'drops': None, 'color': 5, 'team': 2, 'civ': 14, 'civ_alpha': 29, 'won': True}, {'profile_id': 580335, 'steam_id': None, 'name': None, 'clan': None, 'country': None, 'slot': 5, 'slot_type': 1, 'rating': 1236, 
'rating_change': None, 'games': None, 'wins': None, 'streak': None, 'drops': None, 'color': 6, 'team': 2, 'civ': 21, 'civ_alpha': 13, 'won': True}, {'profile_id': 1967010, 'steam_id': None, 'name': None, 
'clan': None, 'country': None, 'slot': 6, 'slot_type': 1, 'rating': 1134, 'rating_change': None, 'games': None, 'wins': None, 'streak': None, 'drops': None, 'color': 3, 'team': 1, 'civ': 25, 'civ_alpha': 9, 
'won': False}]}
'''