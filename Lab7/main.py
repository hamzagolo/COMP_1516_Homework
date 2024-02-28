# Author: Marvin Neoh


sports_leagues = {
    "NFL": "National Football League (American football)",
    "MLB": "Major League Baseball (Baseball)",
    "NBA": "National Basketball Association (Basketball)",
    "EPL": "Premier League (Association football)",
    "NHL": "National Hockey League (Ice hockey)",
    "MLS": "Major League Soccer (Association football)",
    "IPL": "Indian Premier League (Twenty20 cricket)",
    "AFL": "Australian Football League (Australian rules football)",
    "NRL": "National Rugby League (Rugby league football)",
    "CFL": "Canadian Football League (Canadian football)",
}


def delete_league():
    """
    This function deletes the league inputted by the user from the sports_league dictionary.
    """
    to_be_deleted = input("Enter a league to be deleted: ")
    if to_be_deleted not in sports_leagues:
        print(f"There is no league named {to_be_deleted}.")
    else:
        deleted_league = sports_leagues.pop(to_be_deleted)
        print(f"The {deleted_league} has been removed.")


def add_league():
    """
    This function adds the league inputted by the user to the sports_league dictionary.
    """
    league_to_be_added = input("Enter the three-letter abbreviation for a league: ")
    if league_to_be_added in sports_leagues:
        print(f"{league_to_be_added} is already listed as the {sports_leagues[league_to_be_added]}.")
    else:
        league_description = input("Enter the the description of the league: ")
        sports_leagues[league_to_be_added] = league_description


def get_abbreviations():
    """
    This function returns a list of all sports_leagues keys
    :return: Sports_league keys, list
    """
    return sports_leagues.keys()


def get_league_descriptions_tuple():
    """
    This function returns a tuple of all sports_leagues values
    :return:  Sports_leagues values, tuple
    """
    return tuple(sports_leagues.values())


def get_league_descriptions_set():
    """
    This function returns a set of all sports_leagues key and values
    :return: Sports_leagues keys and values, set
    """
    return sports_leagues
