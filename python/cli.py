""" Main file """

import sys
import argparse

from profile_utils import save_profile, load_profile


def execute_command(command, profile):
    """ Executes the target command """
    if command == "save":
        save_profile(profile)
    elif command == "load":
        load_profile(profile)
    else:
        print("Invalid command.")


def main():
    """ Main code execution """

    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="[save, load]")
    parser.add_argument("profile", help="name of profile to use")
    args = parser.parse_args()
    try:
        execute_command(args.command, args.profile)
    except OSError:
        sys.exit(1)


main()
