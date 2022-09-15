from aoe2netapi import AOE2NETAPI

def main():
    """
    This is a script to populate the database with data from July 31st, 2020, to all the way to
    January 1st, 2022.
    """
    api_client = AOE2NETAPI()
    api_client.setup()

    # 1596238991 - July 31st, 2020
    # 1596241038 - Just after July 31st, 2020.
    # 1640995200 - January 1st, 2022

    # Most recent timestamp -
    # 1599429793
    # September 6, 2020

    print("Starting the script.")
    # TODO: Take the information from the savepoint and update the most recent timestamp + api_client.
    api_client.get_all_matches_since_time(since=1599429793, until=1640995200)
    print("Script complete!")

    # Savepoint:
    """
    Match 271df540-a3e2-1145-bfc5-0d53adef5451 has been saved.
    Player 2762511 already exists!
    PlayerMatch [Match: 271df540-a3e2-1145-bfc5-0d53adef5451 - Player: 2762511] has been saved.
    Player 428417 already exists!
    PlayerMatch [Match: 271df540-a3e2-1145-bfc5-0d53adef5451 - Player: 428417] has been saved.
    Player 2768175 already exists!
    PlayerMatch [Match: 271df540-a3e2-1145-bfc5-0d53adef5451 - Player: 2768175] has been saved.
    Player 2300252 already exists!
    PlayerMatch [Match: 271df540-a3e2-1145-bfc5-0d53adef5451 - Player: 2300252] has been saved.
    Player 654714 already exists!
    PlayerMatch [Match: 271df540-a3e2-1145-bfc5-0d53adef5451 - Player: 654714] has been saved.
    Player 1050058 already exists!
    PlayerMatch [Match: 271df540-a3e2-1145-bfc5-0d53adef5451 - Player: 1050058] has been saved.
    """
main()