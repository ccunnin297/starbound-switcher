""" Main file """

import PySimpleGUI as sg

from profile_utils import save_profile, load_profile, get_profiles
from model import State

# Event Functions


def new_profile_clicked():
    profile_name = STATE.get_new_profile_name()
    if profile_name in STATE.get_profiles():
        print("Profile already exists")
        return
    save_profile(profile_name)
    refresh_profiles()
    STATE.set_current_profile(profile_name)
    refresh_selected_profile()


def new_profile_input_updated(text):
    STATE.set_new_profile_name(text)


def save_profile_clicked():
    save_profile(STATE.get_current_profile())


def load_profile_clicked():
    load_profile(STATE.get_current_profile())


def profile_list_item_selected(new_value):
    STATE.set_current_profile(new_value)
    refresh_selected_profile()


def close_window():
    STATE.close_window()


def handle_event(event, values):
    if event == "save":
        save_profile_clicked()
    elif event == "new":
        new_profile_clicked()
    elif event == "new_profile_input_text":
        new_profile_input_updated(values['new_profile_input_text'])
    elif event == "load":
        load_profile_clicked()
    elif event == "profile_list":
        profile_list_item_selected(values['profile_list'])
    elif event == "refresh_profiles":
        refresh_profiles()
    elif event is None:
        close_window()
    else:
        print("Unknown event %s" % event)

# Layout functions


def refresh_profiles():
    STATE.set_profiles(get_profiles())  # TODO: move?
    STATE.get_window().Element("profile_list").Update(
        values=STATE.get_profiles())


def refresh_selected_profile():
    STATE.get_window().Element("profile_label").Update(
        value=STATE.get_current_profile())


def create_layout():
    return [
        [
            sg.Text("Choose an action")
        ],
        [
            sg.Text("Profiles:", key="profile_label")
        ],
        [
            sg.InputText(key="new_profile_input_text", enable_events=True)
        ],
        [
            sg.Button("New", key="new")
        ],
        [
            sg.InputCombo((), size=(
                20, 1), key="profile_list", enable_events=True)
        ],
        [
            sg.Button("Save", key="save")
        ],
        [
            sg.Button("Load", key="load")
        ],
    ]


def refresh_layout():
    refresh_profiles()
    refresh_selected_profile()


# Main
STATE = State(sg.Window("Window Title", create_layout()).Finalize())
refresh_layout()
while STATE.window_is_open():
    EVENT, VALUES = STATE.window.Read()
    handle_event(EVENT, VALUES)


STATE.window.Close()
