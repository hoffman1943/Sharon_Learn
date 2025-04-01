@echo off
call venv\scripts\activate
pytest -v -s .\test_cases\test_admin_login.py --html reports/report.html
