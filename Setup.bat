@echo off

echo Adding Passman to USER PATH...

set "CURRENT_DIR=%~dp0"

:: Get current USER path safely
for /f "tokens=2*" %%a in ('reg query HKCU\Environment /v Path 2^>nul') do set "USERPATH=%%b"

:: Check if already exists
echo %USERPATH% | find /I "%CURRENT_DIR%" >nul
if %ERRORLEVEL%==0 (
    echo Already in PATH.
) else (
    setx Path "%USERPATH%;%CURRENT_DIR%"
    echo Added to PATH.
)

echo.
echo ✅ Setup complete!
echo Restart terminal and run:
echo passman

pause
