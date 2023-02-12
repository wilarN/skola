import os
import random
import time
from datetime import datetime
import json
# import pystyle as ps
import src.external_modified.pystyle_mod as ps
import shutil
import keyboard as keyb

import src.world as world
import src.misc as misc
import src.items as items

import src.sound_manager as SM

# Get current date and time for logging purposes and debugging.
now = datetime.now()
character_list = []
realm_list = []
rooms = []

global player

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
    "weapon_type": "Slash",
    "played_before": False
}

# To make it a bit more safe and clean, keep people out that want to use inappropriate names.
# List taken from reddit top most used swearwords, profanity and slurs. (America)
name_blacklist = ["Fuck"
                  "Fucking"
                  "Nigga"
                  "Nigger"
                  "Bitch"
                  "Dick"
                  "Slut"
                  "Shag"
                  "Slag"
                  "Cock"
                  "Cunt"
                  "Crap"
                  "Ass"
                  "Pussy"
                  "Tit"
                  "Twat"
                  "Minge"
                  "Motherfucker"
                  "Wanker"]


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

def remove_underscores_and_restore_spaces(string_txt: str):
    return string_txt.replace("_", " ")



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


def get_lines(text_obj, colour=None, output: bool = True, instant: bool = True):
    logo_lines = []
    if type(text_obj) == list:
        for line in text_obj[random.randint(0, len(text_obj) - 1)].split("\n"):
            logo_lines.append(line)
    else:
        for line in text_obj.split("\n"):
            logo_lines.append(line)

    if output:
        for line in logo_lines:
            if colour is not None:
                styled_coloured_print(line.center(shutil.get_terminal_size().columns), instant=instant,
                                      colour=colour)
            else:
                styled_coloured_print(line.center(shutil.get_terminal_size().columns), instant=instant)
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
def backpackAddItem(item, amount, chest: bool = False):
    world.flush()
    if not chest:
        ps.Write.Print(text=ps.Center.XCenter(f"{lang.Item_rewarded} {amount} {item.name}!"), color=ps.Colors.cyan,
                       interval=0.01)
    else:
        ps.Write.Print(text=ps.Center.XCenter(f"You got {amount} {item.name}!"), color=ps.Colors.red_to_yellow,
                       interval=0.01)
    # ':' Is used for description separation,
    # ';' Is used for item separation.
    prev_items = check_json_value_settings("backpack")
    if prev_items.__contains__("NULL"):
        update_json_settings("backpack",
                             (remove_spaces_from_string(item.name) + ":" + remove_spaces_from_string(item.description)))
    else:
        update_json_settings("backpack",
                             prev_items + ";" + remove_spaces_from_string(item.name) + ":" + remove_spaces_from_string(
                                 item.description))


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


def play_SFX(sfx: str = None):
    if sfx is None:
        pass


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

    update_json_settings("weapon_type", selected_player.weapon_type)


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


sun_tzu_quotes = ["The wise warrior avoids the battle.",
                  "Build your opponent a golden bridge to retreat across.",
                  "In the midst of chaos, there is also opportunity.",
                  "To know your Enemy, you must become your Enemy.",
                  "Even the finest sword plunged into salt water will eventually rust.",
                  "The greatest victory is that which requires no battle.",
                  "Appear weak when strong and strong when weak.",
                  ""]


def get_random_quote():
    return sun_tzu_quotes[random.randint(0, len(sun_tzu_quotes) - 1)]


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
    player_obj.experience = data["player_experience"]
    player_obj.current_room_index = data["current_room_index"]
    player_obj.weapon_type = data["weapon_type"]
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
    if colour is not None:
        col = colour
    else:
        col = None
    if instant:
        time_delay = 0
    else:
        time_delay = 0.01
    '''
    Default colour "None" --> cyan_to_green
    red --> red
    blue --> cyan
    orange --> orange
    pink --> pink
    yellow --> yellow
    bluegreen --> bluegreen
    purpleblue --> purple to blue gradient
    greenyellow --> greenyellow
    Default instant --> False
    '''
    if colour is None:
        ps.Write.Print(text=ps.Center.XCenter(text), color=ps.Colors.cyan, interval=time_delay)
    else:
        if colour == "red":
            col = ps.Colors.red
        elif colour == "orange":
            col = ps.Colors.orange
        elif colour == "blue":
            col = ps.Colors.cyan
        elif colour == "pink":
            col = ps.Colors.pink
        elif colour == "greenwhite":
            col = ps.Colors.green_to_white
        elif colour == "purpleblue":
            col = ps.Colors.purple_to_blue
        elif colour == "yellow":
            col = ps.Colors.yellow
        elif colour == "bluegreen":
            col = ps.Colors.blue_to_green
        elif colour == "greenyellow":
            col = ps.Colors.green_to_yellow

        ps.Write.Print(text=ps.Center.XCenter(text), color=col, interval=time_delay)
    print("", flush=True)


def styled_coloured_print(text, colour=None, instant=False):
    if colour is not None:
        col = colour
    else:
        col = None
    if instant:
        time_delay = 0
    else:
        time_delay = 0.01
    '''
    Default colour "None" --> cyan_to_green
    red --> red
    blue --> cyan
    orange --> orange
    pink --> pink
    purpleblue --> purple to blue gradient
    green --> green
    greenwhite --> greenwhite
    Default instant --> False
    '''
    if colour is None:
        ps.Write.Print(text=text, color=ps.Colors.cyan_to_green, interval=time_delay)
    else:
        if colour == "red":
            col = ps.Colors.red
        elif colour == "redpurple":
            col = ps.Colors.red_to_purple
        elif colour == "orange":
            col = ps.Colors.orange
        elif colour == "blue":
            col = ps.Colors.cyan
        elif colour == "pink":
            col = ps.Colors.pink
        elif colour == "green":
            col = ps.Colors.green
        elif colour == "greenwhite":
            col = ps.Colors.green_to_white
        elif colour == "purpleblue":
            col = ps.Colors.purple_to_blue
        ps.Write.Print(text=text, color=col, interval=time_delay)
    print("", flush=True)


def styled_thinking_dots(continuous_times: int = 1, colour: str = None, delay: float = 1):
    """
    :param continuous_times: How many times it should repeat the process.
    :param colour: What colour.
    :param delay: In seconds.
    :return return: No return value.
    """
    for i in range(0, continuous_times):
        print("", flush=True)
        if colour is None:
            styled_coloured_print_centered(text="...")
        else:
            styled_coloured_print_centered(text="...", colour=colour)
        time.sleep(delay)
    print("", flush=True)


def styled_line(colour: str = None):
    if colour is None:
        styled_coloured_print_centered(text="-+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-")
    else:
        styled_coloured_print_centered(text="-+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-", colour=colour)


def styled_coloured_print_boxed_centered(text):
    ps.Write.Print(color=ps.Colors.cyan_to_green,
                   text=ps.Box.Box(ps.Center.XCenter(text), up_left="+", left_line="-", right_line="-", up_right="+",
                                   down_right="+",
                                   down_line="-", down_left="+", up_line="-"), interval=0.01)


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


def check_against_blacklisted_words(word: str):
    for name in name_blacklist:
        if word in name.lower():
            print("AAAAAAAAA")
            styled_coloured_print_centered(
                text="Please make sure your name is appropriate.. Try again.")
            return True
        else:
            return False


def check_against_set(word: str, set):
    for i in set:
        if word == i:
            return True
        else:
            pass
    else:
        return False


diff_settings = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}


def create_realm(empty: bool):
    if not empty:
        while True:
            temp_realm_name = styles_input(f"\n{lang.realm_name}", True)
            temp_realm_name = temp_realm_name.lower().strip(" ")
            if temp_realm_name == "" or len(temp_realm_name.strip(" ")) < 3:
                styled_coloured_print_centered(
                    text="Realm name has to be longer than two characters... Please try again...")
                pass
            else:
                break
        while True:
            temp_diff = styles_input(f"\n{lang.difficulty}", True)
            temp_diff = temp_diff.lower().strip(" ")
            if temp_diff == "":
                styled_coloured_print_centered(
                    text="This field cannot be left empty.... Please enter a valid difficulty...")
                pass
            elif check_against_set(word=temp_diff, set=diff_settings):
                break
            else:
                pass

        cur_realm = world.realm(realm_name=remove_spaces_from_string(temp_realm_name), realm_difficulty=temp_diff)

    else:
        cur_realm = world.realm(realm_name="", realm_difficulty="")
    clear()
    return cur_realm


def create_character(empty: bool):
    if not empty:
        while True:
            temp_char_name = styles_input(f"\n{lang.hero_name}", True)
            temp_char_name = temp_char_name.lower().strip(" ")
            if temp_char_name == "" or len(temp_char_name.strip(" ")) < 4:
                styled_coloured_print_centered(
                    text="Name has to be longer than three characters... Please try again...")
                pass
            elif check_against_blacklisted_words(temp_char_name.lower().strip(" ")):
                pass
            else:
                break

        cur_character = misc.player(name=remove_spaces_from_string(temp_char_name), health=100, level=1, mana=100,
                                    status="None", alive=True,
                                    experience=0, current_room_index=0, backpack=None, weapon_type="Default")
        time.sleep(0.5)
        space_down_three_new_lines(True)
        styled_coloured_print_centered(f"{temp_char_name.capitalize()}...", colour="greenwhite")
        time.sleep(2)
        styled_thinking_dots(colour="greenwhite", continuous_times=1, delay=0.5)
        styled_coloured_print_centered(f"What a truly wonderful name...", colour="greenwhite")

        time.sleep(4)
    else:
        cur_character = misc.player(name="", health=100, level=1, mana=100, status="None", alive=True,
                                    experience=0, current_room_index=0, backpack=None, weapon_type="Default")
    return cur_character


def listToString(s):
    """
    Credits geeksforgeeks
    """
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1


def get_format_inventory():
    val = check_json_value_settings("backpack")
    result = val.split(";")
    total_items = []
    for item in result:
        total_items.append(listToString(item).split(":"))
    return total_items


def load_most_recent_room_by_index():
    last_saved_room_index = check_json_value_settings("current_room_index")
    if last_saved_room_index == "NULL":
        return "NULL"
    else:
        try:
            return world.loaded_rooms_indexed[last_saved_room_index]
        except:
            return world.loaded_rooms_indexed["1"]


def space_down_three_new_lines(single=True, five: bool = False):
    """
    Had to make this function since the pystyle writing method had a bug with new line spacing...
    """
    if single:
        print("\n")

    elif five:
        print("\n\n\n\n\n")
    else:
        print("\n\n\n")


def check_inventory():
    global player
    while True:
        clear()
        space_down_three_new_lines()
        get_lines(text_obj=world.sym.sack, output=True, instant=True, colour="purpleblue")

        tempNUM = 1
        all_items_list = []
        all_items_list.clear()
        styled_coloured_print_centered(text="\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-", colour="purpleblue", instant=True)
        styled_coloured_print_centered(text=f"- [ {player.name}'s INVENTORY] -\n", colour="pink")
        items_and_indexed_number_in_list = []
        for item in get_format_inventory():
            styled_coloured_print_centered(f"[{tempNUM}] - {item[0]}", instant=True)
            items_and_indexed_number_in_list.append([tempNUM, item[1]])
            all_items_list.append(item)
            tempNUM += 1

        styled_coloured_print_centered(text="\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-", colour="purpleblue", instant=True)
        space_down_three_new_lines()

        styled_coloured_print_centered(text="(Just press `enter` to continue without selecting a specific item...)",
                                       instant=True)
        usr_sel = styles_input(text=">>", centered=True)
        if usr_sel == "":
            break
        else:
            space_down_three_new_lines()
            for item in items_and_indexed_number_in_list:
                # print(type(str(item[0])))
                if usr_sel == str(item[0]):
                    # Item exists in list
                    styled_coloured_print_centered(text=remove_underscores_and_restore_spaces(item[1]), colour="purpleblue")
                    space_down_three_new_lines()
                    enter_to_continue()
                    clear()
                    break
                else:
                    pass


def damage_player(damage_amount: int):
    cur_value = check_json_value_settings("player_health")
    if cur_value == 0:
        pass
    else:
        new_value = int(cur_value)-damage_amount
        update_json_settings("player_health", int(new_value))


def begin_adventure():
    global player
    player = get_player()
    if check_json_value_settings("player_health") <= 0:
        # Previous death
        update_json_settings("player_health", 100)
        styled_coloured_print_centered(text="\nBecause you died. Half of your hard earned experience points will be removed...", colour="yellow")
        prev = check_json_value_settings("player_experience")
        update_json_settings("player_experience", int((prev/2)))
        enter_to_continue()
        space_down_three_new_lines()
        styled_coloured_print_centered(text="\nYou will now be thrown back a bit before where you left off...", colour="yellow")
        time.sleep(1)
        enter_to_continue()

    # if first_time:
    #     space_down_three_new_lines()
    #     styled_coloured_print_centered(lang.begin_welcome_first_time)
    #     time.sleep(2)
    #

    while True:

        # check_inventory()

        latest = load_most_recent_room_by_index()
        if latest == "NULL":
            world.introduction()

        # If last room:
        if latest == sorted(dict.keys(world.loaded_rooms_indexed))[-1]:
            break
        latest.__call__()

    slow_print(f"{lang.welcome_back} {get_user_data(1)} {lang.welcome_back_2} {get_realm_data(1)}", 0.04)
    # -- Temp disabled, Enable all the world. < room > 's when release. (Little comment reminder for myself).
    # world.dummy_room()
    print("[DEBUG] - TUTORIAL DONE")
    backpackAddItem(items.diamond_sword, 1)
    # world.room01()
