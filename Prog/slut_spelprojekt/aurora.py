# Python general modules
import os

# Game specific modules
import src.headers as headers


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
    main()
