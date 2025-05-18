#!/bin/bash

# Smart Baseball Setup Script for Open Devin
# This script sets up the environment for the Smart Baseball project

set -e  # Exit on error

echo "Setting up Smart Baseball project..."

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cat > .env << EOF
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=baseball
POSTGRES_HOST=db
POSTGRES_PORT=5432
DATABASE_URL=postgresql://postgres:postgres@db:5432/baseball
EOF
    echo ".env file created."
else
    echo ".env file already exists."
fi

# Create required directories
echo "Creating required directories..."
mkdir -p .data
mkdir -p .pybaseball/cache
mkdir -p .pybaseball/core

# Download Lahman dataset if it doesn't exist
if [ ! -f .pybaseball/core/lahman_1871-2023_csv.7z ]; then
    echo "Downloading Lahman dataset..."
    wget -O .pybaseball/core/lahman_1871-2023_csv.7z "https://www.dropbox.com/scl/fi/hy0sxw6gaai7ghemrshi8/lahman_1871-2023_csv.7z?e=2&rlkey=edw1u63zzxg48gvpcmr3qpnhz&dl=1"
    
    # Check if 7z is installed, if not install it
    if ! command -v 7z &> /dev/null; then
        echo "Installing 7zip..."
        apt-get update && apt-get install -y p7zip-full
    fi
    
    # Extract the dataset
    echo "Extracting Lahman dataset..."
    cd .pybaseball/core
    7z x lahman_1871-2023_csv.7z
    cd ../../
else
    echo "Lahman dataset already exists."
fi

echo "Setup complete!"
echo ""
echo "To start the project:"
echo "1. Run 'docker-compose up -d' to start the database and Python services"
echo "2. To run migrations: 'docker-compose exec python alembic upgrade head'"
echo "3. To seed the database: 'docker-compose exec python python seed.py'"
echo ""
echo "The database will be available at localhost:5432"
echo "Username: postgres"
echo "Password: postgres"
echo "Database: baseball"