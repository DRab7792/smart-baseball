# Smart Baseball

A project for analyzing baseball statistics using the Lahman dataset.

## Setup

### Automatic Setup (Recommended)

Run the setup script to automatically configure your environment:

```bash
./setup.sh
```

This script will:
1. Create a `.env` file with default database credentials
2. Download the Lahman dataset
3. Create necessary directories
4. Provide instructions for running the project

### Manual Setup

If you prefer to set up manually:

1. Create a `.env` file with the following content:
```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=baseball
POSTGRES_HOST=db
POSTGRES_PORT=5432
DATABASE_URL=postgresql://postgres:postgres@db:5432/baseball
```

2. Download the Lahman dataset [here](https://www.dropbox.com/scl/fi/hy0sxw6gaai7ghemrshi8/lahman_1871-2023_csv.7z?e=2&rlkey=edw1u63zzxg48gvpcmr3qpnhz&dl=0) and extract it into a directory called `.pybaseball/core`

## Running the Project

1. Start the services:
```bash
docker-compose up -d
```

2. Run database migrations:
```bash
docker-compose exec python alembic upgrade head
```

3. Seed the database:
```bash
docker-compose exec python python seed.py
```