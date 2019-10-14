""" """


class State:
    """ """

    def __init__(self, window):
        self.current_profile = ""
        self.new_profile_name = ""
        self.profiles = ()
        self.window = window
        self.window_open = True

    def get_new_profile_name(self):
        return self.new_profile_name

    def set_new_profile_name(self, profile_name):
        self.new_profile_name = profile_name

    def get_current_profile(self):
        return self.current_profile

    def set_current_profile(self, profile):
        self.current_profile = profile

    def get_profiles(self):
        return self.profiles

    def set_profiles(self, profiles):
        self.profiles = profiles

    def get_window(self):
        return self.window

    def window_is_open(self):
        return self.window_open

    def close_window(self):
        self.window_open = False
