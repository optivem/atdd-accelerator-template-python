@echo off

REM Development startup script for the Python monolith application

echo Starting ATDD Accelerator Template - Python Monolith...

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Run the application
echo Starting the application on http://localhost:8080
python -m uvicorn com.optivem.atddaccelerator.template.monolith.monolith_application:app --host 0.0.0.0 --port 8080 --reload