from pybaseball import team_ids, park_codes
from pybaseball.utils import get_text_file
from sqlalchemy import text
import pandas as pd
from io import StringIO

team_columns = ['teamID', 'lgID', 'city', 'name', 'start_year', 'end_year']

def rs_teams():
    url = "https://www.retrosheet.org/TEAMABR.TXT"
    s = get_text_file(url)
    data = pd.read_csv(StringIO(s), sep=',', quotechar='"')
    data.columns = team_columns
    return data

def seed_teams(db, start_year=2000, end_year=2021):
    for year in range(start_year, end_year + 1):
        teams = team_ids(year)
        print ("*******YEAR: " + str(year))

        # Insert franchises
        franchises = teams['franchID'].unique()
        print (franchises)
        
        values = [{"name": franchise} for franchise in franchises]
        db.execute(
            text("INSERT INTO franchises (name) VALUES (:name) ON CONFLICT (name) DO NOTHING"),
            values
        )
        
        db.commit()

        # Select franchise IDs 
        franchise_ids = db.execute(text("SELECT id, name FROM franchises")).fetchall()
        franchise_dict = {}
        for (id, name) in franchise_ids:
            franchise_dict[name] = id
        

        # Get all data needed for teams table
        rs_team_data = rs_teams()
        rs_team_data = rs_team_data.drop(columns=['lgID'])
        team_data = pd.merge(teams, rs_team_data, left_on='teamIDretro', right_on='teamID', how='left')
        team_data = team_data.rename(columns={'lgID_y': 'lgID'})
        team_data = team_data.drop(columns=['teamID_x'])
        
        # Insert teams
        values = []
        for index, row in team_data.iterrows():
            end_year = None if row['end_year'] == 2021 else row['end_year']
            values.append({
                "league": row['lgID'],
                "name": row['name'],
                "franchise_id": franchise_dict[row['franchID']],
                "fg_id": row['teamIDfg'],
                "br_id": row['teamIDBR'],
                "rs_id": row['teamIDretro'],
                "location": row['city'],
                "start_year": row['start_year'],
                "end_year": end_year,
            })
        db.execute(
            text("INSERT INTO teams (league, name, franchise_id, fg_id, br_id, rs_id, location, start_year, end_year) VALUES (:league, :name, :franchise_id, :fg_id, :br_id, :rs_id, :location, :start_year, :end_year) ON CONFLICT (rs_id) DO NOTHING"),
            values
        )
        
        db.commit()

def seed_franchise_years(db):
    sql = """
        SELECT
            min(teams.start_year) as start_year,
            CASE 
                WHEN bool_or(teams.end_year IS NULL) THEN NULL
                ELSE max(teams.end_year)
            END AS end_year,
            franchises.name as franchise
        FROM teams
        LEFT JOIN franchises ON teams.franchise_id = franchises.id
        GROUP BY franchises.name
    """
    franchise_years = db.execute(text(sql)).fetchall()
    print (franchise_years)