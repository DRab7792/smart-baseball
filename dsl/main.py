import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pybaseball import team_ids

# from models import Base, YourModel  # Replace 'YourModel' with your actual model

DATABASE_URL = os.getenv("DATABASE_URL", "db")

def connect_db():
    engine = create_engine(DATABASE_URL)
    # Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def seed_teams(db):

    # Add your seeding logic here
    # Example:
    # new_entry = YourModel(attribute1="value1", attribute2="value2")
    # session.add(new_entry)
    teams = team_ids(2019)
    print (teams)


if __name__ == "__main__":
    db = connect_db()

    seed_teams(db)

    db.commit()
    db.close()