# Starbound Switcher

## Requirements

Python 3

## Running locally

To ensure dependencies are installed:
`./install.sh`

This command will install `pipenv`, which will then be used to

All debugging should be done in the python directory:
`cd python`

### To install

For new packages / updates:
`pipenv install` or `pipenv install [package name]`

From lock (don't update packages):
`pipenv sync`

### To debug

`pipenv run main.py`

## Creating executable

`./packager.sh`
