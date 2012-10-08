#!/bin/sh

# Check dependencies
command -v python > /dev/null 2>&1 || { echo >&2 "Python not found"; exit 1; }
command -v easy_install > /dev/null 2>&1 || { echo >&2 "Easy Install not found"; exit 1; }

# install pip and Flask
easy_install pip 2>&1 || { echo >&2 "Pip install failed"; exit 1; }
pip install flask 2>&1 || { echo >&2 "Flask install failed"; exit 1; }

# run unit and integration tests for Flask
python flask_unit.py 2>&1 || { echo >&2 "Unit test failed :-("; exit 1; }
python flask_integration.py 2>&1 || { echo >&2 "Integration test failed :-{"; exit 1; }

# if everything is OK, run the app
python hello.py
