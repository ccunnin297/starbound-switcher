#!bin/bash
sh install.sh
cd python
pipenv run python/cli.py "$@"
cd ..
