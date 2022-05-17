import json
import requests


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


# This is just a test method to make sure things work. I will remove this IN TIME.
def main():
    api_client = AOE2NETAPI()
    api_client.setup()

    # print(api_client.fetch_matches(since="1596238991")) # July 31st, 2020
    # print(api_client.fetch_match_details("0d9b38e1-1042-6a4c-bf73-af3221625368"))

main()