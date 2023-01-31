# Python general modules
import os

# Game specific modules
import time

import src.headers as headers

game_version = "Demo 1.0"

"""
##########
## TODO ##
##########
1 - Start adventure CHECK // COMPLETED
2 - Battle-System
> User attack against npc
> npc fight back mechanic, return fire.
> Dodge action

FIX ATTACK COUNTDOWN IN WORLD.PY

3 - Player Effects
4. Work on monster and room object in world. list to keep track of room index etc. // PARTLY COMPLETED
5. add gold
6. MUSICCCCCCCCCCCCCCCCCCCCCC // PARTLY COMPLETED, MUSIC SELECTION STILL REMAINS
7. Try except for external files to make sure it doesn't crash on first run- Just to be safe.

8. Fix die system for npcs.

ATTACK TYPES:
SLASH --> Default, Hand, Sword etc.

CAST --> Magic, Wand, Book.


SHOPKEEPER:
soof --> f.i.l --> Ask O, Deni, Higher prices.



AFTER YOU KILL THE ATTACKED NPC, YOU GET THE MENU INSTEAD OF MOVING ON IN THE STORY (TOO TIRED TO FIX NOW ITS 4AM... THIS FRIENDLY NOTE FOR MYSELF)

"""

global realm
global player

headers.SM.initialise()


def change_windowSize():
    cmd = "mode con: cols=200 lines=50"
    os.system(cmd)


def intro_menu():
    headers.get_lines(text_obj=headers.world.sym.op3x_text, instant=True, output=True, colour="purpleblue")
    # headers.styled_coloured_print_centered(text=f"- AURORA - {game_version}")
    headers.world.flush()
    headers.styled_coloured_print_centered(text="-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    headers.styled_coloured_print_centered(text=f"- AURORA - {game_version}")
    headers.styled_coloured_print_centered(text="-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    time.sleep(1)
    headers.styled_coloured_print_centered(text="-+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-\n"
                                                "+                                                    + \n"
                                                "-       A Terminal indie RPG made by William.J       - \n"
                                                "+                                                    + \n"
                                                "-           This version is far from finished!       - \n"
                                                "+           But I hope you enjoy anyways.            + \n"
                                                "-                                                    - \n"
                                                "+                                                    + \n"
                                                "-    Updates will be available on the github page.   - \n"
                                                "+                                                    + \n"
                                                "-                                                    - \n"
                                                "+-+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+ \n"
                                                "-                                                    - \n"
                                                "+  Credits:                                          + \n"
                                                "-                                                    - \n"
                                                "+     - Music: Toby Fox (UNDERTALE© & DELTARUNE©)    + \n"
                                                "-                                                    - \n"
                                                "+     - Stolen Code: Credits in comments in code     + \n"
                                                "-       above the code snippet in question.          - \n"
                                                "+       (See source code for reference)              + \n"
                                                "-                                                    - \n"
                                                "+-+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+ \n"
                                                "-                                                    - \n"
                                                "+      OBS!!!                                        + \n"
                                                "-      Game progress is saved throughout playing     - \n"
                                                "+      the game automatically.                       + \n"
                                                "-      You might end up losing progress if the       - \n"
                                                "+      terminal window is forcefully closed or if    + \n"
                                                "-      the settings.json file gets corrupted.        - \n"
                                                "+      (So don't mess with the settings.json)(!)     + \n"
                                                "-                                                    - \n"
                                                "+          @wilarN | @william.jsson@hotmail.com      +\n"
                                                "-+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-\n"
                                                "", instant=True, colour="greenwhite")

    headers.space_down_three_new_lines()
    headers.styled_coloured_print_centered(text=f'{headers.get_random_quote()}', instant=False, colour="pink")
    time.sleep(2)
    headers.space_down_three_new_lines(True)
    headers.styled_coloured_print_centered(text="-- Sun Tzu, The Art of War.", instant=True, colour="yellow")

    headers.enter_to_continue()

change_windowSize()

headers.___init()

language = headers.check_json_value_settings("lang")
# User selects translation of game.
while language == "NULL":

    usr_language = input("Swedish or english? - [s/S - e/E]")

    print(
        "[WARNING] - MUST RUN AS SUDO ON LINUX TO FUNCTION, SOME LIBRARIES REQUIRE SUDO PRIVILEGES SUCH AS KEYBOARD DETECTION.")
    headers.enter_to_continue()

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
        headers.space_down_three_new_lines()
        headers.styled_coloured_print_centered(lang.player_begin_adventure)

        # Create Character and save playerdata to settings.json.
        player = headers.create_character(False)
        headers.update_player_save(player)
        headers.clear()
    if headers.check_json_value_settings("currently_selected_realm") == "NULL":
        headers.space_down_three_new_lines()
        headers.styled_coloured_print_centered(lang.realm_begin_adventure)
        realm = headers.create_realm(False)
        headers.update_realm_save(realm)

    else:
        # Load player and realm data from save
        player = headers.get_player()
        realm = headers.get_realm()
        del player
    if not headers.check_json_value_settings("Has_Begun"):
        # Has created realm world, but not yet started the adventure.
        headers.begin_adventure(realm=realm, first_time=True)
        del realm
    else:
        headers.begin_adventure(realm=realm, first_time=False)
        del realm


if __name__ == '__main__':
    intro_menu()
    main()
