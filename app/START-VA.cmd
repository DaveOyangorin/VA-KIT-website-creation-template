@echo off
REM Novarte VA - double-click this file to open your app.
title Novarte VA
cd /d "%~dp0"

where node >nul 2>nul
if errorlevel 1 (
  echo.
  echo   Node.js is not installed on this PC.
  echo   Install it once from https://nodejs.org  ^(the "LTS" button^), then run this file again.
  echo.
  pause
  exit /b 1
)

echo Starting Novarte VA...
start "" http://localhost:5080
node server.js
echo.
echo The app stopped. You can close this window.
pause
