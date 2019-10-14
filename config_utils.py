""" Config related functions """

import json
import os

from os_utils import ensure_file


def is_config_available():
    try:
        get_config()
        return True
    except ValueError:
        return False


def get_config_property(key):
    """ Gets a property from the config """
    config = get_config()
    return config[key]


def set_config_property(key, value):
    """ Updates a property in the config """
    config = get_config()
    config[key] = value
    save_config(config)


def get_config():
    """
    Get config
    Use config.json if available, otherwise use default.json
    """
    path = get_config_path()
    try:
        with open(path) as file:
            return json.load(file)
    except ValueError:
        print("Failed to load json at path: %s" % path)
        raise


def save_config(new_config):
    """ Save config to config.json """

    path = get_user_config_path()
    ensure_file(path)
    with open(path, 'w') as file:
        json.dump(new_config, file, indent=4)


def get_config_path():
    """ Get available config path """
    user_config_path = get_user_config_path()
    if os.path.isfile(user_config_path):
        return user_config_path
    return os.getcwd() + "\\config.default.json"


def get_user_config_path():
    """ Get user config path """
    return os.getcwd() + "\\config.json"
