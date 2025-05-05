from pybaseball import team_ids, park_codes
from pybaseball.utils import get_text_file
from sqlalchemy import text
import pandas as pd
from io import StringIO
from .franchises import get_franchise_dict

team_columns = ['teamID', 'lgID', 'city', 'name', 'start_year', 'end_year']

def truncate_table(db):
    # Truncate teams table with cascade to remove all data and reset id sequence
    db.execute(text("TRUNCATE TABLE teams CASCADE"))
    db.execute(text("ALTER SEQUENCE teams_team_id_seq RESTART WITH 1"))
    db.commit()


def rs_teams():
    url = "https://www.retrosheet.org/TEAMABR.TXT"
    s = get_text_file(url)
    data = pd.read_csv(StringIO(s), sep=',', quotechar='"')
    data.columns = team_columns
    return data

def seed_teams(db, start_year=2000, end_year=2021):
    """Seed teams for the given year range."""
    truncate_table(db)
    franchise_dict = get_franchise_dict(db)
    
    for year in range(start_year, end_year + 1):
        print(f"*******YEAR: {year}")
        teams = team_ids(year)
        
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
                "franchise_id": franchise_dict.get(row['franchID'], 0),
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
    print(franchise_years)