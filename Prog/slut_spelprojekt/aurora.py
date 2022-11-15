# Python general modules
import json
import os
import random
import time
# Game specific modules
import src.world as world
import src.misc as misc
import src.headers as headers
import src.symbols as sym

headers.___init()

language = headers.check_json_value_settings("lang")
# User selects translation of game.
while language == "":
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

    language = headers.check_json_value_settings("lang")
    if language == "se_SE":
        import src.language.se_SE as lang

    else:
        import src.language.en_EN as lang

    # Check if used has already started a session, character or realm.
    # If not, create a character and realm to play in.
    if headers.check_json_value_settings("player_name") == "":
        headers.slow_print(lang.player_begin_adventure, 0.02)

        # Create Character and save playerdata to settings.json.
        player = headers.create_character()
        headers.update_player_save(player)
        headers.clear()
        headers.slow_print(lang.create_realm_text, 0.02)
        headers.create_realm()
    else:
        headers.slow_print(f"Welcome back {os.uname().sysname}.", 0.02)
        player = headers.load_player_save()

    headers.create_realm()

    while True:
        headers.clear()
        # Global Logo
        headers.get_lines(sym.op3x_text, True)
        # Main Menu
        headers.get_lines(lang.menu, True)

        usr_sel = input("~$: ")

        if usr_sel.lower() == "cc":
            continue
        else:
            print("Please Input A Valid Selection!")
            time.sleep(1)


if __name__ == '__main__':
    main()
