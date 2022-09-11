from aoe2net_django.wsgi import *
from aoe2net_database.models import Player, Match
from aoe2netapi import AOE2NETAPI


class PlayerStatistics():
    def __init__(self, player, start_elo, end_elo, civ_picker):
        self.player = player
        self.start_elo = start_elo
        self.end_elo = end_elo
        self.civ_picker = civ_picker

# This whole dang thing should really be a class.
def collect_player_stats():
    # Set up the API Client so we can get a list of civilizations.
    api_client = AOE2NETAPI()
    api_client.setup()
    players = Player.objects.all()

    # Need to collect all of the ranked 1v1 matches as that'll be easiest to determine ELO changes.
    """
    Note: 
    game_type 0 - "Random Map"
    rating_type 2 - "1v1 Random Map"
    """
    ranked_1v1_matches = Match.objects.all().filter(game_type=0, rating_type=2) 
    ranked_1v1_match_ids = [match.id for match in ranked_1v1_matches]

    civ_pickers = []
    non_civ_pickers = []

    i = 0
    for player in players:
        i += 1
        is_civ_picker = False

        player_matches = player.matches.filter(player=player.id, match__in=ranked_1v1_match_ids)

        # Note: I thought about putting the time on the "PlayerMatch" Model,
        # But have decided against it as that really is duplicate information.
        # That, and it really does make sense to have that information on the 
        # Match model.
        player_matches = player_matches.order_by("match__started")

        # Also, we want the player's first 50 matches - that's where
        # most of the improvement would occur I would think.
        # NOTE: I think this slice is causing problems for Django. Maybe.
        # Commented out, for now.
        # player_matches = player_matches[0:50]

        total_matches_played = player_matches.count()

        # If we have less than 10 matches played, then that's just not enough to get
        # data from.
        if total_matches_played < 10:
            continue

        # Brain wave - should we be saving this to a model somehow?
        civ_played_count = {}
        for civilization in api_client.civ_id_dict.keys():
            civ_count = player.matches.filter(player=player.id, civ=civilization).count()
            civ_played_count[civilization] = civ_count

            if civ_count >= (total_matches_played * 0.7):
                is_civ_picker = True

        # This is a very rudimentary way to do this, but we'll just check the ELO
        # of the first and last match.
        # TODO: Perform some analysis which allows us look at the ELOs from match to match.
        # NOTE: We might need to do some sneaky business if the first match doesn't have an
        #       ELO rating.
        if player_matches[0].rating == None:
            first_match = player_matches[1]
        else:
            first_match = player_matches[0]
        last_match = player_matches[total_matches_played - 1]

        # Uggh I don't know about this...
        # This is some last ditch error checking to make sure we can get data.
        if first_match.rating == None or last_match.rating == None:
            continue

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

        if i % 1000 == 0:
            print(f"Working... processed {i} players...")

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
    
def main():
    print("Collecting player statistics...")
    civ_pickers, non_civ_pickers = collect_player_stats()
    print("Beginning the the analysis...")
    run_analysis(civ_pickers, non_civ_pickers)

main()