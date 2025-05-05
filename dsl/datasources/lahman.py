from os import path

import pandas as pd
import requests

CACHE_DIR = "./.pybaseball/cache"
BASE_DIR = "core"

def _get_file(tablename: str, quotechar: str = "'") -> pd.DataFrame:
    f = f'{tablename}'
    data = pd.read_csv(
        f"{path.join(CACHE_DIR, f)}",
        header=0,
        sep=',',
        quotechar=quotechar,
        encoding='latin1'
    )
    return data


# do this for every table in the lahman db so they can exist as separate functions
def parks() -> pd.DataFrame:
    return _get_file('core/Parks.csv')

def all_star_full() -> pd.DataFrame:
    return _get_file("core/AllstarFull.csv")

def appearances() -> pd.DataFrame:
    return _get_file("core/Appearances.csv")

def awards_managers() -> pd.DataFrame:
    return _get_file("contrib/AwardsManagers.csv")

def awards_players() -> pd.DataFrame:
    return _get_file("contrib/AwardsPlayers.csv")

def awards_share_managers() -> pd.DataFrame:
    return _get_file("contrib/AwardsShareManagers.csv")

def awards_share_players() -> pd.DataFrame:
    return _get_file("contrib/AwardsSharePlayers.csv")

def batting() -> pd.DataFrame:
    return _get_file("core/Batting.csv")

def batting_post() -> pd.DataFrame:
    return _get_file("core/BattingPost.csv")

def college_playing() -> pd.DataFrame:
    return _get_file("contrib/CollegePlaying.csv")

def fielding() -> pd.DataFrame:
    return _get_file("core/Fielding.csv")

def fielding_of() -> pd.DataFrame:
    return _get_file("core/FieldingOF.csv")

def fielding_of_split() -> pd.DataFrame:
    return _get_file("core/FieldingOFsplit.csv")

def fielding_post() -> pd.DataFrame:
    return _get_file("core/FieldingPost.csv")

def hall_of_fame() -> pd.DataFrame:
    return _get_file("contrib/HallOfFame.csv")

def home_games() -> pd.DataFrame:
    return _get_file("core/HomeGames.csv")

def managers() -> pd.DataFrame:
    return _get_file("core/Managers.csv")

def managers_half() -> pd.DataFrame:
    return _get_file("core/ManagersHalf.csv")

def master() -> pd.DataFrame:
    # Alias for people -- the new name for master
    return people()

def people() -> pd.DataFrame:
    return _get_file("core/People.csv")

def pitching() -> pd.DataFrame:
    return _get_file("core/Pitching.csv")

def pitching_post() -> pd.DataFrame:
    return _get_file("core/PitchingPost.csv")

def salaries() -> pd.DataFrame:
    return _get_file("contrib/Salaries.csv")

def schools() -> pd.DataFrame:
    return _get_file("contrib/Schools.csv", quotechar='"')  # different here bc of doublequotes used in some school names

def series_post() -> pd.DataFrame:
    return _get_file("core/SeriesPost.csv")

def teams_core() -> pd.DataFrame:
    return _get_file("core/Teams.csv")

def teams_upstream() -> pd.DataFrame:
    return _get_file("upstream/Teams.csv") # manually maintained file

def teams_franchises() -> pd.DataFrame:
    return _get_file("core/TeamsFranchises.csv")

def teams_half() -> pd.DataFrame:
    return _get_file("core/TeamsHalf.csv")