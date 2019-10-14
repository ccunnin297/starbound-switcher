# Starbound Switcher

## Requirements

Python 3

## Running locally

To ensure dependencies are installed:
`./install.sh`

This command will install `pipenv`, which will then be used to install python packages

### To install

For new packages / updates:
`pipenv install` or `pipenv install [package name]`

From lock (don't update packages):
`pipenv sync`

### To debug

`pipenv run main.py`

### Creating executable

`./packager.sh`

Once `dist` has been created, you can distribute by compressing the contents of dist to `starbound-switcher.zip`

## Resources

### Style

Styles using Coolors:

https://coolors.co/20232d-554971-d1d1d1-dbdbdb-397367

### GUI

See PySimpleGUI for more:

https://pysimplegui.readthedocs.io/en/latest/
