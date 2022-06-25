import time
import json
import requests

from aoe2net_django.wsgi import *
from aoe2net_database.models import PlayerMatchStat, Match, Player

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
                match_data = self.fetch_match_details(match['match_uuid'])
                # Grab the player details.
                players = match_data.pop('players')
                match_model = self.insert_match(match_data)
                for player in players:
                    # Can't add a player if they don't have a profile id!
                    if player['profile_id'] is not None:
                        player_model = self.insert_player(player['profile_id'])
                        self.insert_playermatchstat(player, match_model, player_model)

    def get_player_match_history_data(self, profile_id, count=5):
        """
        Given a profile ID, this gets the X most recent matches of said player. Unfortunately, this
        won't get all of the matches. (only up to 1000)
        """
        response = requests.get("https://aoe2.net/api/player/matches?game=aoe2de&profile_id={}&count={}".format(profile_id, count))
        return json.loads(response.content)

    def insert_player(self, profile_id):
        """
        This takes player data and then puts it into the database. If player data
        already exists in the database, then it updates it with additional match data.
        """
        # First check to see if the player already exists in the database.
        # CAUTION - I could see making database calls becoming expensive very quickly...
        player = Player.objects.filter(profile_id=profile_id).first()
        if not player:
            player = Player(
                profile_id=profile_id,
            )
            player.save()
            print("Player {} has been saved.".format(profile_id))
        return player

    def insert_match(self, match_data):
        # First check to see if the Match already exists - if it does, do not add it.
        match = Match.objects.filter(match_uuid=match_data['match_uuid']).first()
        if not match:
            match = Match(
                match_id=match_data['match_id'],
                lobby_id=match_data['lobby_id'],
                match_uuid=match_data['match_uuid'],
                version=match_data['version'],
                name=match_data['name'],
                num_players=match_data['num_players'],
                num_slots=match_data['num_slots'],
                average_rating=match_data['average_rating'],
                cheats=match_data['cheats'],
                full_tech_tree=match_data['full_tech_tree'],
                ending_age=match_data['ending_age'],
                expansion=match_data['expansion'],
                game_type=match_data['game_type'],
                has_custom_content=match_data['has_custom_content'],
                has_password=match_data['has_password'],
                lock_speed=match_data['lock_speed'],
                lock_teams=match_data['lock_teams'],
                map_size=match_data['map_size'],
                map=self.id_map_type_dict[match_data['map_type']],
                map_id=match_data['map_type'],
                population=match_data['pop'],
                ranked=match_data['ranked'],
                leaderboard_id=match_data['leaderboard_id'],
                rating_type=match_data['rating_type'],
                resources=match_data['resources'],
                rms=match_data['rms'],
                scenario=match_data['scenario'],
                server=match_data['server'],
                shared_exploration=match_data['shared_exploration'],
                speed=match_data['speed'],
                starting_age=match_data['starting_age'],
                team_together=match_data['team_together'],
                team_positions=match_data['team_positions'],
                treaty_length=match_data['treaty_length'],
                turbo=match_data['turbo'],
                victory=match_data['victory'],
                victory_time=match_data['victory_time'],
                visibility=match_data['visibility'],
                opened=match_data['opened'],
                started=match_data['started'],
                finished=match_data['finished'],
            )
            match.save()
            print("Match {} has been saved.".format(match_data['match_uuid']))
        return match

    def insert_playermatchstat(self, player_data: dict, match_model: Match, player_model: Player):
        # This is how we actually stuff data into Postgres databases.
        # https://stackoverflow.com/questions/50074690/improperlyconfigured-requested-setting-installed-apps-but-settings-are-not-con
        # First check to see if the PlayerMatchStat already exists - if it does, do not add it.
        player_match_stat = PlayerMatchStat.objects.filter(match=match_model, player=player_model).first()
        if not player_match_stat:
            player_match_stat = PlayerMatchStat(
                civ=self.id_civ_dict[player_data['civ']],
                civ_id=player_data['civ'],
                profile_id=player_data['profile_id'],
                steam_id=player_data['steam_id'],
                name=player_data['name'],
                clan=player_data['clan'],
                country=player_data['country'],
                slot=player_data['slot'],
                slot_type=player_data['slot_type'],
                rating=player_data['rating'],
                rating_change=player_data['rating_change'],
                games=player_data['games'],
                wins=player_data['wins'],
                streak=player_data['streak'],
                drops=player_data['drops'],
                color=player_data['color'],
                team=player_data['team'],
                civ_alpha_id=player_data['civ_alpha'],
                won=player_data['won'],
                match=match_model,
                player=player_model,
                )
            player_match_stat.save()
            print("PlayerMatch [Match: {} - Player: {}] has been saved.".format(match_model.match_uuid, player_data['profile_id']))
        return player_match_stat

# This is just a test method to make sure things work. I will remove this IN TIME.
def main():
    api_client = AOE2NETAPI()
    api_client.setup()

    api_client.get_all_matches_since_time(since=1596238991, until=1640995200)

    """
    Example profile IDs:
    347123
    3006662
    1380246
    406135
    2849622
    """
    # print(api_client.get_player_match_history_data(profile_id=3006662, count=1))

    # TODO: Write a method or something to figure out EPOCH time and stuff. ARGH.
    #       Also, find a way to revert EPOCH to date, and date to EPOCH
    # 1596238991 - July 31st, 2020
    # 1596241038 - Just after July 31st, 2020.
    # 1640995200 - January 1st, 2022

main()