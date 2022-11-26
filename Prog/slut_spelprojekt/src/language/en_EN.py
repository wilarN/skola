import time
from time import sleep

menu = ['''
######################################################################
##                       - Create Character( cc )                   ##
##                       - List Characters( lc )                    ##
##                  ---------------------------------               ##
##                       - Create Realm( cr )                       ##
##                       - List Realms( lr )                        ##
##                  ---------------------------------               ##
##                       - Exit/Terminate(E/e/Q/q)                  ##
######################################################################
''']

player_begin_adventure = "It looks like you haven't yet begun your adventure here in the shadow realm."

realm_begin_adventure = "To begin your adventure, please create the realm you shall then later explore and concur."

realm_begin_diff_selector = "Please select the difficulty of your realm.."

realm_name = "Realm name: "
difficulty = "Difficulty - (1-4 EASY // 4-7 MEDIUM // 7-10 HARD): "

hero_name = "Please select a name for your hero: "

create_realm_text = "Now, let's move on to creating the realm."

begin_welcome = "Welcome"

welcome_back = "Welcome back"
welcome_back_2 = "to"
begin_welcome_first_time = f"Welcome to AURORA, Player. Now that you're ready for your adventure. Let's first start off with a few rules and goals."

rules_and_introduction = "\n-- Goals of AURORA --\n" \
                         "[1] - Gather items from fighting monsters.\n" \
                         "[2] - Talk to NPCs and upgrade your stats and gear!\n" \
                         "[3] - Explore. (But remember, no room you enter will ever be the same...)\n"

very_magestic = "very magestic"

shall_be_remembered_quote = '"And for thy it shall be remembered..."'

press_enter_to_continue = "Press `enter` to continue..."

are_you_ready_to_start = "Now that you've gotten the introduction, Are you ready to start your adventure?"
Press_enter_to_truly_start_adventure = "Press enter to truly start your adventure once and for all..."


you_encountered_a = "You encountered a "

you_find_yourself_staring_at_a_big_door = "You find yourself staring at a big door"

what_do_you_do = "What do you do?"
