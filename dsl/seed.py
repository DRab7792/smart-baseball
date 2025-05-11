import os
from seeds.teams import seed_teams
from seeds.franchises import seed_franchises, seed_franchise_years
from seeds.stadiums import seed_stadiums
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
import argparse
# from models import Base, YourModel  # Replace 'YourModel' with your actual model

DATABASE_URL = os.getenv("DATABASE_URL", "db")

def connect_db():
    engine = create_engine(DATABASE_URL)
    # Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    return session

def parse_comma_param(param_str):
    """Parse a comma-separated parameter into a list of strings."""
    if not param_str:
        return []
    return [item.strip() for item in param_str.split(',')]

def main():
    parser = argparse.ArgumentParser(description='Seed the database with initial data')
    parser.add_argument('--truncate', type=str, help='Comma-separated list of tables to truncate (e.g., "franchises,teams")')
    parser.add_argument('--seeds', type=str, help='Comma-separated list of seeds to run (e.g., "franchises,teams,stadiums")')
    args = parser.parse_args()

    truncates = parse_comma_param(args.truncate) if args.truncate != "*" else ['franchises', 'teams', 'stadiums']
    seeds = parse_comma_param(args.seeds) if args.seeds else ['franchises', 'teams', 'stadiums']
    print (f"Truncates: {truncates}")
    print (f"Seeds: {seeds}")

    db = connect_db()

    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

    # First seed franchises
    if 'franchises' in seeds:
        seed_franchises(db, 'franchises' in truncates)
    
    # Then seed teams
    if 'teams' in seeds:
        print ("Seeding teams")
        seed_teams(db, 1900, 2021, 'teams' in truncates)
    
    # Finally update franchise years
    if 'franchises' in seeds:
        seed_franchise_years(db)
    
    if 'stadiums' in seeds:
        seed_stadiums(db, 'stadiums' in truncates)

    db.commit()
    db.close()

if __name__ == "__main__":
    main()