import os
import random
import time
from datetime import datetime
import json
import pystyle as ps
import shutil
import keyboard as keyb

import src.world as world
import src.misc as misc
import src.items as items

# Get current date and time for logging purposes and debugging.
now = datetime.now()
character_list = []
realm_list = []
rooms = []

# To more easily get file directories of certain files and their contents later on.
game_file_dir = "./files"
base_log_dir = f"{game_file_dir}/logs"
global_log = f"{game_file_dir}/logs/globalLogFile.log"
global_settings_path = f"{game_file_dir}/../settings.json"
global_character_path = f"{game_file_dir}/characters"
global_game_path = f"{game_file_dir}/game"

# Customly generated files (Not generated by the initial creation of the global files).
realm_stats_path = f"{game_file_dir}/game/realm_"

settings = {
    "_comment": "Settings JSON file, Don't Mess with the values if you don't know what you're doing thanks :D",
    "lang": "NULL",
    "currently_selected_realm": "NULL",
    "realm_difficulty": "NULL",
    "game_volume": "1",
    "Has_Begun": False,
    "player_name": "NULL",
    "current_room_index": "NULL",
    "player_health": "NULL",
    "player_mana": "NULL",
    "player_level": "NULL",
    "player_experience": "NULL",
    "player_status": "NULL",
    "player_alive": "NULL",
    "backpack": "NULL",
    "played_before": False
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

    """
    language = check_json_value_settings("lang")
    if language == "se_SE":
        import src.language.se_SE as lang

    else:
        import src.language.en_EN as lang
    """


def remove_spaces_from_string(string_txt: str):
    return string_txt.replace(" ", "_")


def enter_to_continue():
    world.flush()
    styles_input((f"\n\n\n{lang.press_enter_to_continue}"), centered=True)


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
        data = json.dumps(json_file)
    json_file.close()
    return data


def read_from_json_to_obj(json_path: str):
    with open(json_path, "r") as json_file:
        obj = json.load(json_file)
        json_file.close()
    return obj


def get_lines(text_obj, output: bool, instant=False):
    logo_lines = []
    if type(text_obj) == list:
        for line in text_obj[random.randint(0, len(text_obj) - 1)].split("\n"):
            logo_lines.append(line)
    else:
        for line in text_obj.split("\n"):
            logo_lines.append(line)

    if output:
        for line in logo_lines:
            if instant:
                time.sleep(0)
            else:
                time.sleep(0.08)
            styled_centered_print(line.center(shutil.get_terminal_size().columns))
            # print(line)


def reverse_difficulty_number():
    num = int(check_json_value_settings("realm_difficulty"))
    if num == 1:
        return 10
    elif num == 2:
        return 9
    elif num == 3:
        return 8
    elif num == 4:
        return 7
    elif num == 5:
        return 6
    elif num == 6:
        return 5
    elif num == 7:
        return 4
    elif num == 8:
        return 3
    elif num == 9:
        return 2
    elif num == 10:
        return 1
    else:
        return False


def summon_item(name, desc, consumed=False):
    if consumed is not False:
        item = misc.item(name=name, description=desc, consumed=consumed)
    item = misc.item(name=name, description=desc)
    return item


def get_player():
    # Load player and realm data from save
    player = create_character(True)
    player = load_player_save(player)
    return player


def get_realm():
    realm = create_realm(True)
    realm = load_realm_save(realm)
    return realm


def grantXP(amount):
    world.flush()
    ps.Write.Print(text=ps.Center.XCenter(f"{lang.Experience_earned} {amount} {lang.Experience}!"),
                   color=ps.Colors.yellow, interval=0.01)
    prev_xp = check_json_value_settings("player_experience")
    update_json_settings("player_experience", (int(prev_xp) + amount))


# Backpack control
def backpackAddItem(item, amount):
    world.flush()
    ps.Write.Print(text=ps.Center.XCenter(f"{lang.Item_rewarded} {amount} {item.name}!"), color=ps.Colors.cyan,
                   interval=0.01)
    prev_items = check_json_value_settings("backpack")
    if prev_items.__contains__("NULL"):
        update_json_settings("backpack", remove_spaces_from_string(item.name))
    else:
        update_json_settings("backpack", prev_items + ";" + remove_spaces_from_string(item.name))


def backpackRemoveItem():
    # Check if item exists.
    # If exists, remove from save file.
    pass


def backpackGetAllItems():
    '''
    NEEDS FIXXXX ASAPPPPPPPPPPP
    '''
    all_items = check_json_value_settings("backpack")
    items = []
    items.append(all_items.split(";"))
    return items


def clear_all_backpack_items():
    update_json_settings("backpack", "")


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


if os.path.exists(global_settings_path):
    language = check_json_value_settings("lang")
    if language == "se_SE":
        import src.language.se_SE as lang
    else:
        import src.language.en_EN as lang
else:
    ___init()
    language = check_json_value_settings("lang")
    if language == "se_SE":
        import src.language.se_SE as lang
    else:
        import src.language.en_EN as lang


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

    # health
    update_json_settings("player_health", selected_player.health)

    # Level
    update_json_settings("player_level", selected_player.level)

    # XP
    update_json_settings("player_experience", selected_player.experience)

    # Status
    update_json_settings("player_status", selected_player.status)

    # Alive // True _ False
    update_json_settings("player_alive", selected_player.alive)


def update_realm_save(selected_realm):
    update_json_settings("currently_selected_realm", selected_realm.realm_name)

    update_json_settings("realm_difficulty", selected_realm.realm_difficulty)


def get_free_room_index():
    print(rooms)
    if len(rooms) > 0:
        return len(rooms)
    else:
        return False


def get_user_data(player_data_selection: int):
    """"
    1: name
    2: health
    3: level
    """
    if player_data_selection == 1:
        # name
        return check_json_value_settings("player_name")
    elif player_data_selection == 2:
        # health
        return check_json_value_settings("player_health")
    elif player_data_selection == 3:
        # level
        return check_json_value_settings("player_level")


def get_realm_data(realm_data_selection: int):
    """"
    1: name
    2: index
    3: difficulty
    """
    if realm_data_selection == 1:
        # name
        return check_json_value_settings("currently_selected_realm")
    elif realm_data_selection == 2:
        # room index
        return check_json_value_settings("current_room_index")
    elif realm_data_selection == 3:
        # difficulty
        return check_json_value_settings("realm_difficulty")
    else:
        pass


# Used to load player data.
def load_player_save(player_obj):
    data = read_from_json_to_obj(global_settings_path)
    player_obj.name = data["player_name"]
    player_obj.health = data["player_health"]
    player_obj.mana = data["player_mana"]
    player_obj.level = data["player_level"]
    player_obj.status = data["player_status"]
    player_obj.alive = data["player_alive"]
    player_obj.current_room_index = data["current_room_index"]
    return player_obj


def load_realm_save(realm_obj):
    data = read_from_json_to_obj(global_settings_path)
    realm_obj.realm_name = data["currently_selected_realm"]
    realm_obj.realm_difficulty = data["realm_difficulty"]
    return realm_obj


def slow_print(text, delay):
    for char in text:
        print(ps.Colorate.Horizontal(ps.Colors.yellow_to_red, char, 1), end="")
        time.sleep(delay)


def styled_coloured_print_centered(text, colour=None, instant=False):
    '''
    Default colour "None" --> cyan_to_green
    red --> red
    Default instant --> False
    '''
    if not instant:
        if colour is None:
            ps.Write.Print(text=ps.Center.XCenter(text), color=ps.Colors.cyan_to_green, interval=0.01)
        elif colour is "red":
            col = ps.Colors.red
            ps.Write.Print(text=ps.Center.XCenter(text), color=col, interval=0.01)
    else:
        if colour is None:
            ps.Write.Print(text=ps.Center.XCenter(text), color=ps.Colors.cyan_to_green, interval=0.01)
        elif colour is "red":
            col = ps.Colors.red
            ps.Write.Print(text=ps.Center.XCenter(text), color=col, interval=0)
    print("", flush=True)


def styled_centered_print(text):
    print(text.center(shutil.get_terminal_size().columns))


def styled_coloured_print_boxed_lines(text):
    print(ps.Center.XCenter(ps.Box.Lines(ps.Colorate.Horizontal(ps.Colors.yellow_to_red, text))))


def styled_coloured_print_boxed(text):
    ps.Write.Print(color=ps.Colors.cyan_to_green,
                   text=ps.Box.Box(text, up_left="+", left_line="-", right_line="-", up_right="+", down_right="+",
                                   down_line="-", down_left="+", up_line="-"), interval=0.01)


def styles_input(text, centered: bool):
    """
    center? TRUE || FALSE
    
    """
    if centered:
        return ps.Write.Input(color=ps.Colors.yellow_to_red, text=ps.Center.XCenter(text), interval=0.001)
    else:
        return ps.Write.Input(color=ps.Colors.yellow_to_red, text=text, interval=0.001)


def print_with_index(list_to_print: list):
    for char in range(len(list_to_print)):
        print(char, list_to_print[char])


def create_realm(empty: bool):
    if not empty:
        temp_realm_name = styles_input(f"\n{lang.realm_name}", True)
        temp_diff = styles_input(f"\n{lang.difficulty}", True)
        cur_realm = world.realm(realm_name=remove_spaces_from_string(temp_realm_name), realm_difficulty=temp_diff)

    else:
        cur_realm = world.realm(realm_name="", realm_difficulty="")
    clear()
    return cur_realm


def create_character(empty: bool):
    if not empty:
        temp_char_name = styles_input(f"\n{lang.hero_name}", True)
        cur_character = misc.player(name=remove_spaces_from_string(temp_char_name), health=100, level=1, mana=100,
                                    status="None", alive=True,
                                    experience=0, current_room_index=0, backpack=None)
        time.sleep(0.5)
        styled_coloured_print_centered(f"{temp_char_name}... {lang.very_magestic}... {lang.shall_be_remembered_quote}")
        time.sleep(4)
    else:
        cur_character = misc.player(name="", health=100, level=1, mana=100, status="None", alive=True,
                                    experience=0, current_room_index=0, backpack=None)
    return cur_character


def begin_adventure(realm, first_time: bool):
    if first_time:
        styled_coloured_print_centered("\n\n\n" + lang.begin_welcome_first_time)
        time.sleep(2)
        world.introduction()
    else:
        slow_print(f"{lang.welcome_back} {get_user_data(1)} {lang.welcome_back_2} {get_realm_data(1)}", 0.04)
        world.dummy_room()
