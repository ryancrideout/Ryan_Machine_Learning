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
    # 1597590774
    # August 16th, 2020

    print("Starting the script.")
    api_client.get_all_matches_since_time(since=1597009893, until=1640995200)
    print("Script complete!")

    # Savepoint:
    """
    Match cda2b635-2448-2843-94ef-930625028ff0 has been saved.
    Player 2801332 has been saved.
    PlayerMatch [Match: cda2b635-2448-2843-94ef-930625028ff0 - Player: 2801332] has been saved.
    Player 2084019 has been saved.
    PlayerMatch [Match: cda2b635-2448-2843-94ef-930625028ff0 - Player: 2084019] has been saved.
    Player 1502262 has been saved.
    PlayerMatch [Match: cda2b635-2448-2843-94ef-930625028ff0 - Player: 1502262] has been saved.
    Player 1685269 has been saved.
    PlayerMatch [Match: cda2b635-2448-2843-94ef-930625028ff0 - Player: 1685269] has been saved.
    Player 239149 already exists!
    PlayerMatch [Match: cda2b635-2448-2843-94ef-930625028ff0 - Player: 239149] has been saved.
    Player 1376938 already exists!
    PlayerMatch [Match: cda2b635-2448-2843-94ef-930625028ff0 - Player: 1376938] has been saved.
    Player 916167 already exists!
    PlayerMatch [Match: cda2b635-2448-2843-94ef-930625028ff0 - Player: 916167] has been saved.
    Player 3257474 has been saved.
    """
main()