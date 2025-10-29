@echo off
REM FitLife Blog - Quick Start Script for Windows

echo ====================================
echo FitLife Blog - Starting Application
echo ====================================
echo.

REM Check if Docker is installed
docker --version >nul 2>&1
if errorlevel 1 (
    echo Error: Docker is not installed. Please install Docker Desktop first.
    echo Visit: https://docs.docker.com/desktop/windows/install/
    pause
    exit /b 1
)

REM Check if Docker Compose is installed
docker-compose --version >nul 2>&1
if errorlevel 1 (
    echo Error: Docker Compose is not installed. Please install Docker Desktop first.
    pause
    exit /b 1
)

echo Docker and Docker Compose are installed
echo.

echo Stopping existing containers...
docker-compose down

echo.
echo Building Docker images...
docker-compose build

echo.
echo Starting services...
docker-compose up -d

echo.
echo Waiting for services to start (30 seconds)...
timeout /t 30 /nobreak

echo.
echo Seeding database with sample articles...
docker-compose exec -T backend python seed_data.py

echo.
echo ====================================
echo FitLife Blog is now running!
echo ====================================
echo.
echo Access the application:
echo   Frontend:  http://localhost:3000
echo   Backend:   http://localhost:8001
echo   API Docs:  http://localhost:8001/docs
echo.
echo Useful commands:
echo   View logs:        docker-compose logs -f
echo   Stop services:    docker-compose down
echo   Restart:          docker-compose restart
echo.
echo Happy blogging!
echo.
pause
