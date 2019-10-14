#!/bin/bash
rm -rf dist
pipenv run pyinstaller -wF --icon=app.ico main.py
mkdir dist/starbound-switcher
mv dist/main.exe dist/starbound-switcher/starbound-switcher.exe
cp config.default.json dist/starbound-switcher
cp app.ico dist/starbound-switcher
