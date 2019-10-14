""" Main file """

import PySimpleGUI as sg

from profile_utils import save_profile, load_profile
from model import State

# Event Functions


def new_profile_clicked():
    profile_name = STATE.get_new_profile_name()
    if profile_name in STATE.get_profiles():
        print("Profile already exists")
        return
    save_profile(profile_name)
    STATE.set_current_profile(profile_name)
    refresh_profiles()
    refresh_current_profile()


def new_profile_input_updated(text):
    STATE.set_new_profile_name(text)


def save_profile_clicked():
    if STATE.get_current_profile() not in STATE.get_profiles():
        return
    save_profile(STATE.get_current_profile())


def load_profile_clicked():
    if STATE.get_selected_profile() not in STATE.get_profiles():
        return
    load_profile(STATE.get_selected_profile())
    STATE.set_current_profile(STATE.get_selected_profile())
    refresh_current_profile()


def profile_list_item_selected(new_value):
    STATE.set_selected_profile(new_value)


def starbound_path_changed(new_value):
    STATE.set_starbound_path(new_value)


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
    elif event == "starbound_path_label":
        starbound_path_changed(values['starbound_path_label'])
    elif event is None:
        close_window()
    else:
        print("Unknown event %s" % event)

# Layout functions


def refresh_profiles():
    STATE.get_window().Element("profile_list").Update(
        values=STATE.get_profiles())


def refresh_current_profile():
    STATE.get_window().Element("profile_label").Update(
        value=STATE.get_current_profile())


def refresh_starbound_path():
    STATE.get_window().Element("starbound_path_label").Update(
        value=STATE.get_starbound_path())


def create_layout():
    return [
        [
            sg.Text('Starbound path:'),
        ],
        [
            sg.FolderBrowse(key="starbound_path_browse",
                            target="starbound_path_label"),
            sg.InputText("", key="starbound_path_label",
                         enable_events=True, disabled=True)
        ],
        [
            sg.Text("", key="profile_label", auto_size_text=False)
        ],
        [
            sg.InputCombo((), size=(
                20, 1), key="profile_list", enable_events=True),
            sg.Button("Save", key="save"),
            sg.Button("Load", key="load")
        ],
        [
            sg.InputText(key="new_profile_input_text", enable_events=True),
            sg.Button("New", key="new")
        ],

    ]


def refresh_layout():
    refresh_profiles()
    refresh_current_profile()
    refresh_starbound_path()


# Main
STATE = State(sg.Window("Starbound Switcher", create_layout()).Finalize())
refresh_layout()
while STATE.window_is_open():
    EVENT, VALUES = STATE.window.Read()
    handle_event(EVENT, VALUES)


STATE.window.Close()
