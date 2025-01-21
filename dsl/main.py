import os
from seeds.teams import seed_teams, seed_franchise_years
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
# from models import Base, YourModel  # Replace 'YourModel' with your actual model

DATABASE_URL = os.getenv("DATABASE_URL", "db")

def connect_db():
    engine = create_engine(DATABASE_URL)
    # Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    return session


if __name__ == "__main__":
    db = connect_db()

    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

    # seed_teams(db, 1900)
    seed_franchise_years(db)
    # parks = park_codes()
    # print(parks)


    db.commit()
    db.close()