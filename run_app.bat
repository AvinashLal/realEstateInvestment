@echo off
REM Ensure pipenv is installed and in the PATH
pipenv --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Pipenv is not installed. Please install pipenv first.
    exit /b 1
)

REM Change to the directory where main.py is located
cd /d C:\Users\Avi\coding\realEstateInvestment

REM Set PYTHONPATH to the project root
SET PYTHONPATH=C:\Users\Avi\coding\realEstateInvestment

REM Install dependencies if Pipfile.lock or Pipfile has changed
pipenv install

REM Run the FastAPI application using pipenv
pipenv run uvicorn app.main:app --reload
