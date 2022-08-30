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
    # 1597720006
    # August 18th, 2020

    print("Starting the script.")
    api_client.get_all_matches_since_time(since=1597590774, until=1640995200)
    print("Script complete!")

    # Savepoint:
    """
    Match c3fc10ac-0b8a-ef4c-9d28-809b8bee51c4 has been saved.
    Player 1143932 already exists!
    PlayerMatch [Match: c3fc10ac-0b8a-ef4c-9d28-809b8bee51c4 - Player: 1143932] has been saved.
    Player 712233 already exists!
    PlayerMatch [Match: c3fc10ac-0b8a-ef4c-9d28-809b8bee51c4 - Player: 712233] has been saved.
    """
main()