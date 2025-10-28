#!/bin/bash

# Development startup script for the Python monolith application

echo "Starting ATDD Accelerator Template - Python Monolith..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run the application
echo "Starting the application on http://localhost:8080"
python -m uvicorn com.optivem.atddaccelerator.template.monolith.monolith_application:app --host 0.0.0.0 --port 8080 --reload