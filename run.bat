@echo off
call venv\scripts\activate
pytest -v -s -m .\test_cases\test_admin_login.py --html reports/report.html
