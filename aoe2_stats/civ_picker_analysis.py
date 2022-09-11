from aoe2net_django.wsgi import *
from aoe2net_database.models import Player, Match, PlayerMatchStat
from aoe2netapi import AOE2NETAPI
# Match, PlayerMatchStat

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
    ranked_1v1_matches = Match.objects.all().filter(game_type=0, rating_type=2) # 5670 # 42016 # 9510
    # print(Match.objects.all().filter(rating_type=2, game_type=0).count())
    # print(Match.objects.all().filter(rating_type=0, game_type=0).count())
    ranked_1v1_match_ids = [match.id for match in ranked_1v1_matches]

    """
    itemset_list = [itemset1, itemset2, itemset3]
    itemset_list_ids = [itemset.id for itemset in itemset_list]
    itemset_queryset = ItemSet.objects.filter(id__in=itemset_list_ids)
    items = Item.objects.filter(itemsets__in=itemset_queryset)
    """

    # print(api_client.game_type_id_dict)
    """
    {'Random Map': 0, 'Regicide': 1, 'Death Match': 2, 'Scenario': 3, 'King of the Hill': 6, 'Wonder Race': 7, 'Defend the Wonder': 8, 
    'Turbo Random Map': 9, 'Capture the Relic': 10, 'Sudden Death': 11, 'Battle Royale': 12, 'Empire Wars': 13, 'Co-Op Campaign': 15}
    """
    # Need to filter out the MATCHES based on this. Hrrmm...
    # Do I want 1v1 Random Map
    # OR
    # 1v1 Random Map Quick Play?
    """
    print(api_client.rating_type_id_dict)
    {'Unranked': 0, '1v1 Death Match': 1, '1v1 Random Map': 2, 'Team Death Match': 3, 'Team Random Map': 4, '1v1 Random Map Quick Play': 5, 
    'Team Random Map Quick Play': 6, '1v1 Empire Wars Quick Play': 7, 'Team Empire Wars Quick Play': 8, 'Battle Royale Quick Play': 9, '1v1 Empire Wars': 13, 
    'Team Empire Wars': 14}
    """

    # Prep the data?
    civ_pickers = []
    non_civ_pickers = []

    i = 0
    for player in players:
        i += 1
        is_civ_picker = False

        player_matches = player.matches.filter(player=player.id, match__in=ranked_1v1_match_ids)
        # print(player_matches.count())

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
        # print(total_matches_played) # Not sure what to do yet if less than 50 matches.

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
        # NOTE: We might need to do some sneaky business if the first match doesn't have an
        #       ELO rating.
        if player_matches[0].rating == None:
            first_match = player_matches[1]
        else:
            first_match = player_matches[0]
        last_match = player_matches[total_matches_played - 1]

        # print("We're getting ratings, right?")
        # # print(player_matches) # Okay this is fine...
        # print(first_match.rating) # Have to make sure we have 1v1's and we are ranked.
        # # print(first_match.match.ranked)
        # # map_map = Match.objects.all().filter(id=first_match.match) 
        # # print(map_map.ranked)
        # print(last_match.rating)
        # # map_map = Match.objects.all().filter(id=last_match.match) 
        # # print(map_map.ranked)
        # # print(last_match.match.ranked)

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
    print("Collecting player statistics...")
    civ_pickers, non_civ_pickers = collect_player_stats()
    print("Beginning the the analysis...")
    run_analysis(civ_pickers, non_civ_pickers)

main()