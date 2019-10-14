""" Steam related functions """

import webbrowser

STEAM_WORKSHOP_URL = "https://steamcommunity.com/app/211820/workshop/"


def open_steam_workshop():
    webbrowser.open_new_tab(STEAM_WORKSHOP_URL)
