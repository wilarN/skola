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
    if headers.check_json_value_settings("currently_selected_realm") == "":
        headers.slow_print(lang.realm_begin_adventure, 0.02)
        realm = headers.temp_create_realm()
        print(realm.realm_name, realm.realm_difficulty)
        headers.update_realm_save(realm)

    else:
        if not headers.check_json_value_settings("Has_Begun"):
            # Has created realm world, but not yet started the adventure.
            headers.slow_print(lang.create_realm_text, 0.02)


        else:
            pass
        # Load player data here later.
        # player = headers.load_player_save()
        # headers.slow_print(f"Welcome back {player.name}.", 0.02)
        headers.slow_print(f"Welcome back Player.", 0.02)

    # headers.create_realm()

    while True:
        headers.clear()
        # Global Logo
        headers.get_lines(sym.op3x_text, True)
        # Main Menu
        headers.get_lines(lang.menu, True)

        usr_sel = input("~$: ")

        if usr_sel.lower() == "cc":
            continue
            # headers.create_character()

        elif usr_sel.lower() == "q" or usr_sel.lower() == "e":
            # Save and exit
            print("Exiting...")
            exit(0)

        else:
            print("Please Input A Valid Selection!")
            time.sleep(1)


if __name__ == '__main__':
    main()
