#!/bin/bash
pipenv run pyinstaller -wF main.py
mv dist/main.exe dist/starbound-switcher.exe
cp config.default.json dist
