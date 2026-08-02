@echo off
echo [1/3] Cleaning old Sphinx build cache...
python -m sphinx -M clean . _build

echo [2/3] Building HTML documentation...
python -m sphinx -b html . _build/html
if errorlevel 1 (
    echo.
    echo [ERROR] Build failed! Check the messages above.
    pause
    exit /b
)

echo [3/3] Starting local web server...
start "" http://localhost:8000/index.html
python -m http.server --directory _build/html