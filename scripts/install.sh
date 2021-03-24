# Upgrade pip
python3 -m pip install --upgrade pip
# Install build deps
python3 -m pip install setuptools wheel twine
# If requirements.txt exists, install from it
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
# Install the package from setup.py
python3 setup.py install
