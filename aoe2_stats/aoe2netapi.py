import time
import json
import requests

from aoe2net_django.wsgi import *
from aoe2net_database.models import PlayerMatchStat

class AOE2NETAPI():
    """
    The API I will use to collect data from https://aoe2.net/#. I will build upon this
    as I need more functionality.

    TODO: Make an EPOCH Class?
    TODO: Add functionality to get specific player classes.
    """
    def __init__(self):
        # TODO: Evaluate if this is how we want to store these variables. 
        #       Something about this screams "BAD IDEA" to me...
        # Civilizations
        self.id_civ_dict = {}
        self.civ_id_dict = {}
        # Victory conditions
        self.id_victory_dict = {}
        self.victory_id_dict = {}
        # Game Types
        self.id_game_type_dict = {}
        self.game_type_id_dict = {}
        # Starting Age
        self.id_age_dict = {}
        self.age_id_dict = {}
        # Map Type. E.G., Arabia, Nomad, etc.
        self.id_map_type_dict = {}
        self.map_type_id_dict = {}
        # Rating Types
        self.id_rating_type_dict = {}
        self.rating_type_id_dict = {}
        # Starting Resources
        self.id_resource_dict = {}
        self.resource_id_dict = {}
        # Game Speed
        self.id_speed_dict = {}
        self.speed_id_dict = {}
        # Visibility Settings. E.G., Fully Visible, Explored, etc.
        self.id_visibility_dict = {}
        self.visibility_id_dict = {}
        # Map Size
        self.id_map_size_dict = {}
        self.map_size_id_dict = {}
        # Languages - I could implement this, but for now we're all in English baby.
        '''
        self.id_language_dict = {}
        self.language_id_dict = {}
        '''
        # Leaderboard - I think this has to do with rankings?
        self.id_leaderboard_dict = {}
        self.leaderboard_id_dict = {}

    def setup(self):
        """
        General set up of things we should do before we get this party started.
        """
        self.fetch_api_dicts()

    def fetch_api_dicts(self):
        """
        The reason why I have this as a separate method is becaues there may be more civilizations, game types,
        etc. could be added in the future, so we can't hard code it and it should be updated from time to time.

        Further note: There are some parameters in here that I didn't bother saving. Namely just the language one
                      for now, as I'm going to do this all in English first.

        # TODO: Write some dang unit tests for these bad boys. Good grief.
        """
        response = requests.get("https://aoe2.net/api/strings?game=aoe2de&language=en") # Put this in a class somehow?
        api_strings = json.loads(response.content)
        # Set the civilizations
        civilizations = api_strings['civ']
        for civ in civilizations:
            self.id_civ_dict[civ["id"]] = civ["string"] 
            self.civ_id_dict[civ["string"]] = civ["id"]

        # Set the victory strings
        victory_conditions = api_strings['victory']
        for victory_condition in victory_conditions:
            self.id_victory_dict[victory_condition["id"]] = victory_condition["string"]
            self.victory_id_dict[victory_condition["string"]] = victory_condition["id"]

        # Set the game types
        game_types = api_strings['game_type']
        for game_type in game_types:
            self.id_game_type_dict[game_type["id"]] = game_type["string"]
            self.game_type_id_dict[game_type["string"]] = game_type["id"]

        # Set the age settings
        age_settings = api_strings['age']
        for age_setting in age_settings:
            self.id_age_dict[age_setting["id"]] = age_setting["string"]
            self.age_id_dict[age_setting["string"]] = age_setting["id"]

        # Set the map types.
        map_types = api_strings['map_type']
        for map_type in map_types:
            self.id_map_type_dict[map_type["id"]] = map_type["string"]
            self.map_type_id_dict[map_type["string"]] = map_type["id"]

        # Set the rating types
        rating_types = api_strings['rating_type']
        for rating_type in rating_types:
            self.id_rating_type_dict[rating_type["id"]] = rating_type["string"]
            self.rating_type_id_dict[rating_type["string"]] = rating_type["id"]

        # Set the resources settings
        resources_settings = api_strings['resources']
        for resource_setting in resources_settings:
            self.id_resource_dict[resource_setting["id"]] = resource_setting["string"]
            self.resource_id_dict[resource_setting["string"]] = resource_setting["id"]

        # Set the speed settings
        speed_settings = api_strings['speed']
        for speed_setting in speed_settings:
            self.id_speed_dict[speed_setting["id"]] = speed_setting["string"]
            self.speed_id_dict[speed_setting["string"]] = speed_setting["id"]

        # Set the visibility settings
        visibility_settings = api_strings['visibility']
        for visibility_setting in visibility_settings:
            self.id_visibility_dict[visibility_setting["id"]] = visibility_setting["string"]
            self.id_visibility_dict[visibility_setting["string"]] = visibility_setting["id"]

        # Set the map sizes
        map_sizes = api_strings['map_size']
        for map_size in map_sizes:
            self.id_map_size_dict[map_size["id"]] = map_size["string"]
            self.map_size_id_dict[map_size["string"]] = map_size["id"]

        # Set the leaderboard types.
        leaderboards = api_strings['map_size']
        for leaderboard in leaderboards:
            self.id_leaderboard_dict[leaderboard["id"]] = leaderboard["string"]
            self.leaderboard_id_dict[leaderboard["string"]] = leaderboard["id"]

    def fetch_matches(self, since=None, count=10):
        """
        Fetches matches from a specific epoch time. Ideally we go through and then check the specific
        details of the match to get further information.
        """
        response = requests.get("https://aoe2.net/api/matches?game=aoe2de&count={}&since={}".format(count, since)) 
        return json.loads(response.content)

    def fetch_match_details(self, match_id):
        """
        Gather specific information from a match. This is how we'll gather win rates and other information.
        """
        response = requests.get("https://aoe2.net/api/match?uuid={}".format(match_id)) 
        return json.loads(response.content)

    def get_all_matches_since_time(self, since=None, until=None):
        # Initial timestamp
        timestamp = since
        # Safety precaution if 'until' isn't set so we don't have infinite recursion.
        if not until:
            # Cast to int first to remove rounding errors.
            until = int(time.time())

        # This is the meat and the potatoes of the method.
        while timestamp < until:
            matches = self.fetch_matches(since=timestamp)
            # Sort matches based on timestamp, 
            sorted_matches = sorted(matches, key=lambda dict: dict['started'])
            for match in sorted_matches:
                timestamp = match['started']
                match_details = self.fetch_match_details(match['match_uuid'])
                print(match_details.keys()) # I think initially this is what we're interested in, we could get more match details later though.
                print(match_details)
                '''
                dict_keys([
                    'match_id', 'lobby_id', 'match_uuid', 'version', 'name', 'num_players', 'num_slots', 'average_rating', 'cheats', 'full_tech_tree', 'ending_age', 'expansion', 'game_type', 
                    'has_custom_content', 'has_password', 'lock_speed', 'lock_teams', 'map_size', 'map_type', 'pop', 'ranked', 'leaderboard_id', 'rating_type', 'resources', 'rms', 'scenario', 
                    'server', 'shared_exploration', 'speed', 'starting_age', 'team_together', 'team_positions', 'treaty_length', 'turbo', 'victory', 'victory_time', 'visibility', 'opened', 
                    'started', 'finished', 'players'])
                '''
                '''
                {
                    'match_id': '32257097', 
                    'lobby_id': None, 
                    'match_uuid': 'b6472ffc-bb5b-7649-bbe0-88a7e96e1886', 
                    'version': None, 
                    'name': 'AUTOMATCH', 
                    'num_players': 4, 
                    'num_slots': 4, 
                    'average_rating': None, 
                    'cheats': False, 
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
                        {'profile_id': 2421746, 'steam_id': None, 'name': None, 'clan': None, 'country': None, 'slot': 1, 'slot_type': 1, 'rating': 1358, 'rating_change': None, 'games': None, 'wins': None, 'streak': None, 'drops': None, 'color': 4, 'team': 1, 'civ': 3, 'civ_alpha': 11, 'won': True}, 
                        {'profile_id': 2384128, 'steam_id': None, 'name': None, 'clan': None, 'country': None, 'slot': 2, 'slot_type': 1, 'rating': 1247, 'rating_change': None, 'games': None, 'wins': None, 'streak': None, 'drops': None, 'color': 1, 'team': 2, 'civ': 12, 'civ_alpha': 24, 'won': False}, 
                        {'profile_id': 3165630, 'steam_id': None, 'name': None, 'clan': None, 'country': None, 'slot': 3, 'slot_type': 1, 'rating': None, 'rating_change': None, 'games': None, 'wins': None, 'streak': None, 'drops': None, 'color': 2, 'team': 1, 'civ': 8, 'civ_alpha': 25, 'won': True}, 
                        {'profile_id': 1493900, 'steam_id': None, 'name': None, 'clan': None, 'country': None, 'slot': 4, 'slot_type': 1, 'rating': 1246, 'rating_change': None, 'games': None, 'wins': None, 'streak': None, 'drops': None, 'color': 3, 'team': 2, 'civ': 13, 'civ_alpha': 6, 'won': False}
                        ]
                    }
                '''

    def insert_data_django():
        # This is how we actually stuff data into Postgres databases.
        # https://stackoverflow.com/questions/50074690/improperlyconfigured-requested-setting-installed-apps-but-settings-are-not-con
        chump_data = PlayerMatchStat(civ="Teutons", civ_id=99)
        # chump_data.save()

# This is just a test method to make sure things work. I will remove this IN TIME.
def main():
    api_client = AOE2NETAPI()
    api_client.setup()

    # api_client.get_all_matches_since_time(since=1596238991, until=1596241038)

    # api_client.insert_data_django() # Alright this works like a dream. Now we need to clean this sucker up.

    # TODO: Write a method or something to figure out EPOCH time and stuff. ARGH.
    #       Also, find a way to revert EPOCH to date, and date to EPOCH
    # 1596238991 - July 31st, 2020
    # 1596241038 - Just after July 31st, 2020.

main()