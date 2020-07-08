start "start-backend" cmd /c "python manage.py runserver"
cd frontend
start "start-fronend" cmd /c "npm run serve"

rem pause>nul
