from pybaseball import team_ids
from datasources.lahman import teams_franchises
from sqlalchemy import text

def truncate_table(db):
    # Truncate franchises table with cascade to remove all data and reset id sequence
    db.execute(text("TRUNCATE TABLE franchises CASCADE"))
    db.execute(text("ALTER SEQUENCE franchise_id_seq RESTART WITH 1"))
    db.commit()

def seed_franchises(db):
    """Seed franchises from Lahman and Retrosheet data."""
    truncate_table(db)

    # Get all unique franchise IDs from Retrosheet
    teams = team_ids(2021)  # Using 2021 as a reference year to get all franchises
    rs_franchises = teams['franchID'].unique()
    
    # Get Lahman franchises
    lh_franchises = teams_franchises()
    
    # Prepare franchise values
    values = [{"name": franchise[1], "lh_id": franchise[0]} for franchise in lh_franchises.values]
    # Find RS franchises that don't have corresponding Lahman franchise records
    missing_franchises = [{"name": rs_id, "lh_id": rs_id} for rs_id in rs_franchises if not any(rs_id == franchise[0] for franchise in lh_franchises.values)]
    values.extend(missing_franchises)

    # Insert franchises
    db.execute(
        text("INSERT INTO franchises (lh_id, name) VALUES (:lh_id, :name) ON CONFLICT (lh_id) DO NOTHING"),
        values
    )
    db.commit()
    
    return get_franchise_dict(db)

def get_franchise_dict(db):
    """Get a dictionary mapping franchise IDs to their database IDs."""
    franchise_ids = db.execute(text("SELECT id, lh_id FROM franchises")).fetchall()
    return {lh_id: id for (id, lh_id) in franchise_ids}

def seed_franchise_years(db):
    """Update franchise years based on team data."""
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

    # Update franchises with their active years
    for year_data in franchise_years:
        db.execute(
            text("""
                UPDATE franchises 
                SET start_year = :start_year,
                    end_year = :end_year
                WHERE name = :franchise
            """),
            {
                "start_year": year_data.start_year,
                "end_year": year_data.end_year,
                "franchise": year_data.franchise
            }
        )
    db.commit()

    return franchise_years