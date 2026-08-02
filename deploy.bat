@echo off
echo Stage all modified files...
git add .

echo Commit changes...
git commit -m "Update project files and fix Sphinx extension config"

echo Push to GitHub...
git push origin main

echo.
echo Process complete!
pause