# Python general modules
import time
import os


import pygame
pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("src/sfx/Kirby.wav")
sound.set_volume(0.2)
sound.play()

# Game specific modules
import src.headers as headers
import src.symbols as sym

"""
##########
## TODO ##
##########
1 - Start adventure CHECK
2 - Battle-System
3 - Player Effects
4. Work on monster and room object in world. list to keep track of room index etc.
5. add gold
6. MUSICCCCCCCCCCCCCCCCCCCCCC
"""

global realm
global player


def change_windowSize():
    cmd = "mode con: cols=200 lines=50"
    os.system(cmd)


change_windowSize()

headers.___init()

language = headers.check_json_value_settings("lang")
# User selects translation of game.
while language == "NULL":
    usr_language = input("Swedish or english? - [s/S - e/E]")

    if usr_language.lower() == "e":
        headers.update_json_settings("lang", "en_EN")
        import src.language.en_EN as lang

    elif usr_language.lower() == "s":
        headers.update_json_settings("lang", "se_SE")
        import src.language.se_SE as lang
    else:
        print("Please select a valid language.")
    # Check if language value has been changed else stay in loop and keep asking.
    language = headers.check_json_value_settings("lang")
    print(language)


def main():
    global realm
    global player
    language = headers.check_json_value_settings("lang")
    if language == "se_SE":
        import src.language.se_SE as lang

    else:
        import src.language.en_EN as lang

    # Check if used has already started a session, character or realm.
    # If not, create a character and realm to play in.
    headers.clear()
    if headers.check_json_value_settings("player_name") == "NULL":
        headers.styled_coloured_print_centered(lang.player_begin_adventure)

        # Create Character and save playerdata to settings.json.
        player = headers.create_character(False)
        headers.update_player_save(player)
        headers.clear()
    if headers.check_json_value_settings("currently_selected_realm") == "NULL":
        headers.styled_coloured_print_centered(lang.realm_begin_adventure)
        realm = headers.create_realm(False)
        headers.update_realm_save(realm)

    else:
        # Load player and realm data from save
        player = headers.create_character(True)
        player = headers.load_player_save(player)

        realm = headers.create_realm(True)
        realm = headers.load_realm_save(realm)
    if not headers.check_json_value_settings("Has_Begun"):
        # Has created realm world, but not yet started the adventure.
        headers.begin_adventure(realm=realm, first_time=True)
    else:
        headers.begin_adventure(realm=realm, first_time=False)

"""
    while True:
        headers.clear()
        # Global Logo
        headers.get_lines(sym.op3x_text, True)
        # Main Menu
        headers.get_lines(lang.menu, True)

        usr_sel = input("~$: ")

        if usr_sel.lower().__contains__("cc"):
            continue
            # headers.create_character()

        elif usr_sel.lower().__contains__("q") or usr_sel.lower().__contains__("e"):
            # Save and exit
            print("Exiting...")
            exit(0)

        else:
            print("Please Input A Valid Selection!")
            time.sleep(1)
"""

if __name__ == '__main__':
    main()
