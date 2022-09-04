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
    # 1598642973
    # August 28th, 2020

    print("Starting the script.")
    # TODO: Take the information from the savepoint and update the most recent timestamp + api_client.
    api_client.get_all_matches_since_time(since=1598642973, until=1640995200)
    print("Script complete!")

    # Savepoint:
    """
    Match b405b003-7e8a-114b-aca1-e987341619ec has been saved.
    Player 2413814 already exists!
    PlayerMatch [Match: b405b003-7e8a-114b-aca1-e987341619ec - Player: 2413814] has been saved.
    Player 2753748 already exists!
    PlayerMatch [Match: b405b003-7e8a-114b-aca1-e987341619ec - Player: 2753748] has been saved.
    Player 2023988 already exists!
    PlayerMatch [Match: b405b003-7e8a-114b-aca1-e987341619ec - Player: 2023988] has been saved.
    Player 1986425 already exists!
    PlayerMatch [Match: b405b003-7e8a-114b-aca1-e987341619ec - Player: 1986425] has been saved.
    Player 2908959 already exists!
    PlayerMatch [Match: b405b003-7e8a-114b-aca1-e987341619ec - Player: 2908959] has been saved.
    Player 3317419 already exists!
    PlayerMatch [Match: b405b003-7e8a-114b-aca1-e987341619ec - Player: 3317419] has been saved.
    Player 3185575 already exists!
    PlayerMatch [Match: b405b003-7e8a-114b-aca1-e987341619ec - Player: 3185575] has been saved.
    Player 1898052 already exists!
    PlayerMatch [Match: b405b003-7e8a-114b-aca1-e987341619ec - Player: 1898052] has been saved.
    """
main()