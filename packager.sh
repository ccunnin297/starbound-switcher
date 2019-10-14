#!bin/bash
sh install.sh
cd python
pipenv run pyinstaller -wF main.py
mv dist ..
cd ..
