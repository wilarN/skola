# Python general modules
import json
import os
import random
import time
# Game specific modules
import src.world as world
import src.misc as misc
import src.headers as header
import src.symbols as sym

language = header.check_json_value_settings("lang")
# User selects translation of game.
while language == "":
    usr_language = input("Swedish or english? - [s/S - e/E]")

    if usr_language.lower() == "e":
        header.update_json_settings("lang", "en_EN")
        import src.language.en_EN as lang

    elif usr_language.lower() == "s":
        header.update_json_settings("lang", "se_SE")
        import src.language.se_SE as lang
    else:
        print("Please select a valid language.")
    # Check if language value has been changed else stay in loop and keep asking.
    language = header.check_json_value_settings("lang")
    print(language)


def main():

    header.___init()
    header.update_json_settings("player_name", "test_player_name")

    # Check if used has already started a session, characted or realm.
    # If not, create a character and realm to play in.
    if header.check_json_value_settings("Has_Begun") == "False":
        header.slow_print("It looks like you haven't yet begun your adventure here in the shadow realm.\n"
                          "Please start by creating your hero.", 0.02)

        # Create Character and save playerdata to settings.json.
        player = header.create_character()
        header.update_player_save(player)
        header.clear()
        header.slow_print("Now, let's move on to creating the realm.", 0.02)
    else:
        header.slow_print(f"Welcome back {os.uname().sysname}.", 0.02)
        player = header.load_player_save()

    header.create_realm()

    while True:
        header.clear()
        # Global Logo
        header.get_lines(sym.op3x_text, True)
        # Main Menu
        header.get_lines(lang.menu, True)

        usr_sel = input("~$: ")

        if usr_sel.lower() == "cc":
            continue
        else:
            print("Please Input A Valid Selection!")
            time.sleep(1)


if __name__ == '__main__':
    main()
