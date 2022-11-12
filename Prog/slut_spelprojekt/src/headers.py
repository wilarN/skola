import os
import random
import time
from datetime import datetime
import json

import src.world as world
import src.misc as misc

# Get current date and time for logging purposes and debugging.
now = datetime.now()

character_list = []
realm_list = []

# To more easily get file directories of certain files and their contents later on.
game_file_dir = "./files"
base_log_dir = f"{game_file_dir}/logs"
global_log = f"{game_file_dir}/logs/globalLogFile.log"
global_settings_path = f"{game_file_dir}/../settings.json"
global_character_path = f"{game_file_dir}/characters"
global_game_path = f"{game_file_dir}/game"

settings = {
    "_comment": "Settings JSON file, Don't Mess with the values if you don't know what you're doing thanks :D",
    "lang": "",
    "currently_selected_realm": "",
    "game_volume": "1",
    "Has_Begun": "False",
    "player_name": "",
    "player_mana": "",
    "player_level": "",
    "player_experience": "",
    "player_status": "",
    "player_alive": ""
}


def ___init():
    # To automate creating files and directories for the project. Lists for dynamic adding and removing stuff for later.
    file_keep_count = [global_log]
    dirs_keep_count = [base_log_dir, game_file_dir, global_character_path, global_game_path]

    # Two below actually executes the creation of the files and dirs.
    for i in dirs_keep_count:
        if not os.path.exists(i):
            os.makedirs(i)

    for i in file_keep_count:
        if not os.path.exists(i):
            file = open(i, "w+")
            file.close()

    # Initialize the settings.json file containing global settings parameters but also some user stats and params.
    if not os.path.exists(global_settings_path):
        json_settings = json.dumps(settings, indent=4)

        with open("settings.json", "w") as jsonfile:
            jsonfile.write(json_settings)
        jsonfile.close()


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def logOutput(msg, logType):
    # Log
    if logType == 1:
        # print("\n[ LOG ] " + msg)
        write_to_file("\n[LOG] " + msg, global_log, "a+")
    # Error
    elif logType == 2:
        # print("\n[ ERROR ] " + msg)
        write_to_file("\n[ERROR] " + msg, global_log, "a+")
    # Warning
    elif logType == 3:
        # print("\n[ WARNING ] " + msg)
        write_to_file("\n[WARNING] " + msg, global_log, "a+")


def read_from_json(json_path: str):
    with open(json_path, "r") as json_file:
        data = json.load(json_file)
    json_file.close()
    return data


def get_lines(text_obj, output: bool):
    logo_lines = []
    if type(text_obj) == list:
        for line in text_obj[random.randint(0, len(text_obj) - 1)].split("\n"):
            logo_lines.append(line)
    else:
        for line in text_obj.split("\n"):
            logo_lines.append(line)

    if output:
        for line in logo_lines:
            time.sleep(0.1)
            print(line)


def write_to_file(text_to_write, path_to_file, typeOfWrite):
    if os.path.exists(path_to_file):
        write_file = open(path_to_file, typeOfWrite)
        write_file.write(text_to_write)
        write_file.close()


def update_json_settings(key, new_value):
    settings_file = open(global_settings_path, "r")
    json_obj = json.load(settings_file)
    settings_file.close()
    json_obj[f"{key}"] = new_value
    settings_file = open(global_settings_path, "w")
    json.dump(json_obj, settings_file, indent=4)
    settings_file.close()


def check_json_value_settings(key):
    settings_file = open(global_settings_path, "r")
    json_obj = json.load(settings_file)
    settings_file.close()
    return json_obj[key]


# Used to save player data.
def update_player_save(selected_player):
    # data = read_from_json(global_settings_path)
    # temp_user_data = selected_player.get_all_stats()
    # usr_data = vars(selected_player)

    # save_data = vars(selected_player)

    # Honestly have no idea how to do this without hardcoding it, aNywAys--- it'll work for now i'm tired and it's 3am.-
    # Username
    update_json_settings("player_name", selected_player.name)

    # Mana
    update_json_settings("player_mana", selected_player.mana)

    # Level
    update_json_settings("player_level", selected_player.level)

    # XP
    update_json_settings("player_experience", selected_player.experience)

    # Status
    update_json_settings("player_status", selected_player.status)

    # Alive // True _ False
    update_json_settings("player_alive", selected_player.alive)


# Used to load player data.
def load_player_save():
    data = read_from_json(global_settings_path)



def slow_print(text, delay):
    for char in text:
        print(char, end="")
        time.sleep(delay)


def print_with_index(list_to_print: list):
    for char in range(len(list_to_print)):
        print(char, list_to_print[char])


def create_realm():
    cur_realm = world.realm(realm_name=input("Realm name: "), realm_difficulty=input("Difficulty: "))


def create_character():
    temp_char_name = input("Please select a name for your hero: ")
    cur_character = misc.player(name=temp_char_name, level=0, mana=100, status="None", alive=True, experience=0)
    return cur_character
