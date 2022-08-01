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
    # 1596514493
    # August 4th, 2020
    print("Starting the script.")
    api_client.get_all_matches_since_time(since=1596514493, until=1640995200)
    print("Script complete!")

    # Savepoint:
    """
    Match 6baf388f-b7b2-7246-a391-711feb10c1b4 has been saved.
    Player 2688268 already exists!
    PlayerMatch [Match: 6baf388f-b7b2-7246-a391-711feb10c1b4 - Player: 2688268] has been saved.
    Player 270492 has been saved.
    PlayerMatch [Match: 6baf388f-b7b2-7246-a391-711feb10c1b4 - Player: 270492] has been saved.
    Player 2686183 already exists!
    PlayerMatch [Match: 6baf388f-b7b2-7246-a391-711feb10c1b4 - Player: 2686183] has been saved.
    Player 1094730 has been saved.
    PlayerMatch [Match: 6baf388f-b7b2-7246-a391-711feb10c1b4 - Player: 1094730] has been saved.
    """
main()