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
        self.id_civ_dict = {}
        self.civ_id_dict = {}

    def setup(self):
        """
        General set up of things we should do before we get this party started.
        """
        self.fetch_civ_dicts()

    def fetch_civ_dicts(self):
        """
        The reason why I have this as a separate method is becaues there may be more civilizations added
        in the future, so we can't hard code it and it should be updated from time to time.
        """
        response = requests.get("https://aoe2.net/api/strings?game=aoe2de&language=en") # Put this in a class somehow?
        api_strings = json.loads(response.content)
        civilizations = api_strings['civ']
        for civ in civilizations:
            self.id_civ_dict[civ["id"]] = civ["string"] 
            self.civ_id_dict[civ["string"]] = civ["id"]

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

    def insert_data_django():
        # This is how we actually stuff data into Postgres databases.
        # https://stackoverflow.com/questions/50074690/improperlyconfigured-requested-setting-installed-apps-but-settings-are-not-con
        chump_data = PlayerMatchStat(civ="Teutons", civ_id=99)
        # chump_data.save()

# This is just a test method to make sure things work. I will remove this IN TIME.
def main():
    api_client = AOE2NETAPI()
    api_client.setup()

    api_client.get_all_matches_since_time(api_client=api_client, since=1596238991, until=1596241038)

    # api_client.insert_data_django() # Alright this works like a dream. Now we need to clean this sucker up.

    # TODO: Write a method or something to figure out EPOCH time and stuff. ARGH.
    #       Also, find a way to revert EPOCH to date, and date to EPOCH
    # 1596238991 - July 31st, 2020
    # 1596241038 - Just after July 31st, 2020.

main()