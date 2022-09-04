from aoe2net_database.models import Player
from aoe2netapi import AOE2NETAPI
# Match, PlayerMatchStat

class PlayerStatistics():
    def __init__(self, player, start_elo, end_elo, civ_picker):
        self.start_elo = 0
        self.end_elo = 0
        self.civ_picker = False
        self.player = None

# This whole dang thing should really be a class.
def collect_player_stats():
    # Set up the API Client so we can get a list of civilizations.
    api_client = AOE2NETAPI()
    api_client.setup()
    players = Player.objects.all()

    # Prep the data?
    civ_pickers = []
    non_civ_pickers = []

    for player in players:
        is_civ_picker = False

        player_matches = player.matches
        # ARGH WE STILL NEED THE TIME THING.
        player_matches.order_by('TIME THAT WE DO NOT HAVE')

        # Also, we want the player's first 50 matches - that's where
        # most of the improvement would occur I would think.
        player_matches = player_matches[0:50]

        total_matches_played = player_matches.count()
        print(total_matches_played) # Not sure what to do yet if less than 50 matches.

        # Brain wave - should we be saving this to a model somehow?
        civ_played_count = {}
        for civilization in api_client.civ_id_dict.keys():
            civ_count = player_matches.filter(civ=civilization).count()
            civ_played_count = civ_played_count[civilization] = civ_count

            if civ_count >= (total_matches_played * 0.7):
                is_civ_picker = True

        # This is a very rudimentary way to do this, but we'll just check the ELO
        # of the first and last match.
        first_match = player_matches[0]
        last_match = player_matches[-1]        

        player_statistic = PlayerStatistics(
            player, 
            first_match.rating,
            last_match.rating,
            is_civ_picker
        )

        if is_civ_picker:
            civ_pickers.append(player_statistic)
        else:
            non_civ_pickers.append(player_statistic)

    return civ_pickers, non_civ_pickers

def run_analysis(civ_pickers, non_civ_pickers):
    print("There were this many civ_pickers:")
    print(len(civ_pickers))
    print("There were this many non_civ_pickers:")
    print(len(non_civ_pickers))
    print()

    # This very likely won't be the same length - will have to investigate
    # weighted averages for statistics. For now though, I'll be lazy.
    # TODO: Ask Timo or someone else that is science smart.
    civ_picker_differences = []
    non_civ_picker_differences = []

    for civ_picker in civ_pickers:
        civ_picker_differences.append(
            civ_picker.end_elo - civ_picker.start_elo
        )

    for non_civ_picker in non_civ_pickers:
        non_civ_picker_differences.append(
            non_civ_picker.end_elo - non_civ_picker.start_elo
        )

    civ_picker_average = sum(civ_picker_differences) / len(civ_pickers)

    non_civ_picker_average = sum(non_civ_picker_differences) / len(non_civ_pickers)

    # NOTE: Would be worthwhile to do this analysis at different ELO brackets.
    print("The average ELO change for civ pickers was:")
    print(civ_picker_average)
    print("The average ELO change for NON civ pickers was:")
    print(non_civ_picker_average)
    
    """
    What we need:
    - People who play one civilization (70% pick rate I'd say)
    - How their ELO changes. Once we have the players we just note the average change.
      - So... start point versus end point? We might miss information here, may be worth recording the individual games + what they played each game + ELO fluctation.
      - Do they LOSE ELO when they're not playing their civilization?

    Hard part - querying the data from Django in an intelligent way.
    Ideas?

    For Player in Players:
        query PlayerMatches based on Player_ID
        Sort them by time, if possible? Time data is on Match... probably should add a field on PlayerStat for "time" and then make a script to populate that. 
        OKAY so we have sorted PlayerMatches:
            Tally up how many matches they played + what civilization they played. Keep track of number of times each civilization was played.
                Maybe we just take the first 20 or 50 games of each?
            If one civilization accounts for 70% more of total games, Player is a civ picker. Otherwise, non-civpicker. 

    Once we have civ pickers and non-civ pickers...
    We need a slice of maybe... 20 games?
        Need to make sure those slice of 20 games follow the 70% rule.
        Also need to note where the ELO starts at. If someone is 1400 and another is 900, I don't know if that's telling.
            Maybe we can have different brackets of ELO. Like, 1000 - 1050, 1051 - 1100, etc. Could combine brackets if we have to.

        Beyond that, just make averages of the ELO shift. Hopefully this ends up being informative.
    """
def main():
    civ_pickers, non_civ_pickers = collect_player_stats()
    run_analysis(civ_pickers, non_civ_pickers)

main()