""" Profile related functions """

from os_utils import create_folder, replace_directory_recursive, list_subfolder_names

STARBOUND_PATH = "E:\\Program Files (x86)\\Steam\\steamapps\\common\\Starbound"

MODS_PATH = STARBOUND_PATH+"\\mods"
STORAGE_PATH = STARBOUND_PATH+"\\storage"

SWITCHER_PATH = STARBOUND_PATH+"\\starbound_switcher"

PROFILE_MODS_FOLDER = "\\mods"
PROFILE_STORAGE_FOLDER = "\\storage"


def get_profiles():
    """ Returns list of current profiles """
    return list_subfolder_names(SWITCHER_PATH)


def get_profile_path(profile_name):
    """ Returns the path for the profile """
    return SWITCHER_PATH + "\\" + profile_name


def create_profile_directory(profile_name):
    """ Create folders for a profile """
    create_folder(SWITCHER_PATH)
    profile_path = get_profile_path(profile_name)
    create_folder(profile_path)


def save_profile(profile_name):
    """ Saves current starbound install to profile folder """
    create_profile_directory(profile_name)
    profile_path = get_profile_path(profile_name)
    replace_directory_recursive(MODS_PATH, profile_path + PROFILE_MODS_FOLDER)
    replace_directory_recursive(
        STORAGE_PATH, profile_path + PROFILE_STORAGE_FOLDER)


def load_profile(profile_name):
    """
    Loads profile to current starbound folder
    WARNING: This overwrites current starbound mods+storage
    """
    profile_path = get_profile_path(profile_name)
    replace_directory_recursive(
        profile_path + PROFILE_MODS_FOLDER, MODS_PATH)
    replace_directory_recursive(
        profile_path + PROFILE_STORAGE_FOLDER, STORAGE_PATH)
