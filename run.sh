#!/bin/bash

# Get the directory of the current script in the main repository
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Change directory to the main repository
cd "$REPO_DIR" || exit

# Pull latest changes from GitHub
echo "Pulling latest changes from GitHub..."
git pull

# Define the virtual environment directory
VENV_DIR="$REPO_DIR/health_venv"

# Check if the virtual environment directory exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    virtualenv -p python3.11 $VENV_DIR
else
    echo "Virtual environment already exists."
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source $VENV_DIR/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r "requirements.txt"

# Run the primary script
echo "Running primary script..."
python3 "scripts/check_search_endpoint.py"