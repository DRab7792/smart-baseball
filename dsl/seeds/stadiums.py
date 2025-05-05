from pybaseball import team_ids, park_codes
from datasources.lahman import *

def seed_stadiums():
    # parks = park_codes()
    ballparks = teams_franchises()
    print (ballparks)
    return ballparks