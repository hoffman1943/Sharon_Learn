@echo off
call venv\scripts\activate
pytest -v -s -m --html reports/report.html
pause
