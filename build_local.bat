@echo off
echo Building Sphinx Documentation...

REM 1. Clean and build the local HTML files
sphinx-build -b html content _build/html

echo.
echo Build complete! Starting local server...
echo Access your site at: http://localhost:8000
echo (Press CTRL+C in this window to stop the server)
echo.

REM 2. Launch local HTTP server to view the site
python -m http.server 8000 --directory _build/html

pause