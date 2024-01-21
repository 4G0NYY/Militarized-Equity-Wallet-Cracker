@echo off

echo Installing dependencies...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo Failed to install dependencies. Exiting.
    exit /b %errorlevel%
)

echo Dependencies installed successfully.
echo Starting the application...
py index.py
