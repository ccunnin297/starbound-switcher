#!bin/bash
cd python
pip install pipenv
pipenv sync --bare --keep-outdated
cd ..
