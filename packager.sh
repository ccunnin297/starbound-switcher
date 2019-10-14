#!/bin/bash
rm -rf dist
pipenv run pyinstaller -wF --icon=app.ico main.py
mv dist/main.exe dist/starbound-switcher.exe
cp config.default.json dist
cp app.ico dist
