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
    # TODO: Take the information from the savepoint and update the most recent timestamp + api_client.
    api_client.get_all_matches_since_time(since=1597720006, until=1640995200)
    print("Script complete!")

    # Savepoint:
    """
    Match a73e70e2-8e6f-274b-a13a-9f031343ffc8 has been saved.
    Player 2905582 already exists!
    PlayerMatch [Match: a73e70e2-8e6f-274b-a13a-9f031343ffc8 - Player: 2905582] has been saved.
    Player 304001 already exists!
    PlayerMatch [Match: a73e70e2-8e6f-274b-a13a-9f031343ffc8 - Player: 304001] has been saved.
    Player 784758 already exists!
    PlayerMatch [Match: a73e70e2-8e6f-274b-a13a-9f031343ffc8 - Player: 784758] has been saved.
    Player 233587 already exists!
    PlayerMatch [Match: a73e70e2-8e6f-274b-a13a-9f031343ffc8 - Player: 233587] has been saved.
    Player 505903 already exists!
    PlayerMatch [Match: a73e70e2-8e6f-274b-a13a-9f031343ffc8 - Player: 505903] has been saved.
    Player 2896055 already exists!
    PlayerMatch [Match: a73e70e2-8e6f-274b-a13a-9f031343ffc8 - Player: 2896055] has been saved.
    """
main()