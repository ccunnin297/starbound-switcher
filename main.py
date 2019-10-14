""" Main file """

import PySimpleGUI as sg

from profile_utils import save_profile, load_profile, delete_profile
from steam_utils import open_steam_workshop
from model import State

# Event Functions


def new_profile_clicked():
    profile_name = STATE.get_new_profile_name()
    if not profile_name or profile_name == "":
        print("Profile missing name")
        return
    if profile_name in STATE.get_profiles():
        print("Profile already exists")
        return
    save_profile(profile_name)
    STATE.set_current_profile(profile_name)
    refresh_profiles()
    refresh_current_profile()
    STATE.set_selected_profile(profile_name)
    refresh_selected_profile()
    STATE.get_window().Element("new_profile_input_text").Update(value="")


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

    show_workshop_popup()


def show_workshop_popup():
    workshop_text = """
    When loading a new profile, you'll need to make sure the correct mods are installed in Steam Workshop.

    Hint: You can make this easier in the future by saving mods intended for a profile as a collection.

    Open Steam Workshop page now?"
    """
    result = sg.PopupOKCancel(workshop_text)

    if result == "OK":
        open_steam_workshop()


def delete_profile_clicked():
    if STATE.get_selected_profile() not in STATE.get_profiles():
        return

    popup_text = """
    Are you sure you want to delete the following profile?

    %s

    This cannot be undone.
    """ % STATE.get_selected_profile()
    result = sg.PopupOKCancel(popup_text)
    if result != "OK":
        return

    if STATE.get_selected_profile() == STATE.get_current_profile():
        STATE.set_current_profile("")
        refresh_current_profile()

    delete_profile(STATE.get_selected_profile())
    refresh_profiles()

    # Set profile back to first
    if len(STATE.get_profiles()) == 0:
        STATE.set_selected_profile("")
    else:
        STATE.set_selected_profile(STATE.get_profiles()[0])


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
    elif event == "delete":
        delete_profile_clicked()
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
    current_profile_text = "Current: %s" % STATE.get_current_profile()
    STATE.get_window().Element("profile_label").Update(
        value=current_profile_text)


def refresh_selected_profile():
    try:
        index = STATE.get_profiles().index(STATE.get_current_profile())
    except ValueError:
        # If value isn't in list, can't perform update
        return
    STATE.get_window().Element("profile_list").Update(set_to_index=index)


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
            sg.Button("Load", key="load"),
            sg.Button("Delete", key="delete")
        ],
        [
            sg.InputText(key="new_profile_input_text", enable_events=True),
            sg.Button("New", key="new")
        ],

    ]


def refresh_layout():
    refresh_profiles()
    refresh_current_profile()
    refresh_selected_profile()
    refresh_starbound_path()


def set_style():
    purple = "#554971"
    grey = "#20232D"
    light_grey = "#D1D1D1"
    lighter_grey = "#DBDBDB"

    background_color = grey
    text_color = lighter_grey
    dark_text_color = grey
    button_color = (text_color, purple)
    input_color = light_grey

    icon_path = "starbound_icon.png"

    sg.SetOptions(icon=icon_path,
                  background_color=background_color,
                  element_background_color=background_color,
                  text_element_background_color=background_color,
                  input_elements_background_color=input_color,
                  button_color=button_color,
                  text_color=text_color,
                  input_text_color=dark_text_color,
                  element_text_color=dark_text_color)


set_style()
STATE = State(sg.Window("Starbound Switcher", create_layout()).Finalize())
refresh_layout()
while STATE.window_is_open():
    EVENT, VALUES = STATE.window.Read()
    handle_event(EVENT, VALUES)


STATE.window.Close()
