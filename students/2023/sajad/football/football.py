import requests


def get_data_list(url: str, key: str) -> list[str]:
    """
    Send request to url and extract the key from retrived data and return it.
    :param url: url of the request.
    :param key: key of the dict
    :return: return a dict contain values.
    """
    request = requests.get(url)
    data = request.json()
    value = data.get(key)
    return value


def get_data_dict(
    url: str, key: str
) -> list[dict[str, str | dict[str, dict[str, str]]]]:
    """
    Send request to url and extract the key from retrived data and return it.
    :param url: url of the request.
    :param key: key of the dict
    :return: return a dict contain values.
    """
    request = requests.get(url)
    data = request.json()
    value = data.get(key)
    return value


def list_years() -> list[str]:
    """
    Returns list of played years.
    return: list of years
    """
    return get_data_list(
        "http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api", "seasons"
    )


def list_teams(year: str) -> list[str]:
    """
    Returns list of aviable teams
    :param year: Year of the game
    return: list of teams' name
    """
    return get_data_list(
        f"http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api/{year}",
        "teams",
    )


def list_gamedays(year: str) -> list[str]:
    """
    Returns list of played game days (months).
    :param year: the year of the game days
    return: list of gamedays (months game played)
    """
    return get_data_list(
        f"http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api/{year}",
        "gamedays",
    )


def list_games(year, month: str) -> list[dict[str, str | dict[str, dict[str, str]]]]:
    """
    Returns list of aviable game days.
    :param year: the year of the game days
    :param month: the month of the game days
    return: list of played games.
    """
    return get_data_dict(
        f"http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api/{year}/{month}",
        "games",
    )


def get_game_result(game, team_result):
    """Decide is the game result winner, loser or draw"""
    home= game["score"]["home"]
    away= game["score"]["away"]
    if home["goals"] > away["goals"]:
        team_result.get(home["team"])["wins"] += 1
        team_result.get(home["team"])["points"] += 3
        team_result.get(away["team"])["lose"] += 1

    if home["goals"] == away["goals"]:
        team_result.get(home["team"])["draw"] += 1
        team_result.get(away["team"])["draw"] += 1
        team_result.get(away["team"])["points"] += 1
        team_result.get(home["team"])["points"] += 1


def calculate_score(year: str):
    """Calculate score of a season (year)"""
    team_result = {}
    for team in list_teams(year):
        team_result.update({team: {"wins": 0, "lose": 0, "draw": 0, "points": 0}})
    for month in list_gamedays(year):
        for game in list_games(year, month):
            get_game_result(game, team_result)

    return team_result

x = calculate_score("2014")
print(x)
