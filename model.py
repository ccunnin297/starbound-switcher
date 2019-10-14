""" """

from config_utils import get_config_property, set_config_property, is_config_available
from profile_utils import get_profiles


class State:
    """ """

    def __init__(self, window):
        self.selected_profile = self.get_current_profile()
        self.new_profile_name = ""
        self.window = window
        self.window_open = True

    def get_new_profile_name(self):
        return self.new_profile_name

    def set_new_profile_name(self, profile_name):
        self.new_profile_name = profile_name

    def get_selected_profile(self):
        return self.selected_profile

    def set_selected_profile(self, profile):
        self.selected_profile = profile

    def get_profiles(self):
        return get_profiles()

    def get_starbound_path(self):
        if not is_config_available():
            return ""
        return get_config_property("starbound_path")

    def set_starbound_path(self, path):
        set_config_property("starbound_path", path)

    def get_current_profile(self):
        if not is_config_available():
            return ""
        return get_config_property("current_profile")

    def set_current_profile(self, profile):
        set_config_property("current_profile", profile)

    def get_window(self):
        return self.window

    def window_is_open(self):
        return self.window_open

    def close_window(self):
        self.window_open = False
