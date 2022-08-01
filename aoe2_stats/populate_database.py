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
    Player 313908 has been saved.
    PlayerMatch [Match: 4ae95078-a1f3-664e-8ac0-e2da3d853a06 - Player: 313908] has been saved.
    Player 528154 has been saved.
    PlayerMatch [Match: 4ae95078-a1f3-664e-8ac0-e2da3d853a06 - Player: 528154] has been saved.
    """
main()