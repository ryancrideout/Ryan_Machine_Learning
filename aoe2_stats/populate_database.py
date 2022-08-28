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
    # 1596994958
    # August 9th, 2020

    print("Starting the script.")
    api_client.get_all_matches_since_time(since=1596994958, until=1640995200)
    print("Script complete!")

    # Savepoint:
    """
    Match 461766c6-a7ce-2045-856a-ad1c40686bee has been saved.
    Player 2589306 already exists!
    PlayerMatch [Match: 461766c6-a7ce-2045-856a-ad1c40686bee - Player: 2589306] has been saved.
    Player 2898768 already exists!
    PlayerMatch [Match: 461766c6-a7ce-2045-856a-ad1c40686bee - Player: 2898768] has been saved.
    Player 2209305 already exists!
    PlayerMatch [Match: 461766c6-a7ce-2045-856a-ad1c40686bee - Player: 2209305] has been saved.
    Player 2155445 already exists!
    PlayerMatch [Match: 461766c6-a7ce-2045-856a-ad1c40686bee - Player: 2155445] has been saved.
    Player 252391 already exists!
    PlayerMatch [Match: 461766c6-a7ce-2045-856a-ad1c40686bee - Player: 252391] has been saved.
    Player 3031980 has been saved.
    PlayerMatch [Match: 461766c6-a7ce-2045-856a-ad1c40686bee - Player: 3031980] has been saved.
    """
main()