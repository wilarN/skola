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

player_begin_adventure = "It looks like you haven't yet begun your adventure here in AURORA."

realm_begin_adventure = "To begin your adventure, please create the realm you shall then later explore and concur."

realm_begin_diff_selector = "Please select the difficulty of your realm.."

realm_name = "Realm name: "
difficulty = "Difficulty - (1-4 EASY // 4-7 MEDIUM // 7-10 HARD): "

hero_name = "Please select a name for your hero: "

woke_up = "You woke up..."
not_knowing = "Not knowing what, and where you are..."

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

shall_be_remembered_quote = '"And by your name we shall pray..."'

press_enter_to_continue = "Press `enter` to continue..."

are_you_ready_to_start = "Now that you've gotten the introduction, Are you ready to start your adventure?"
Press_enter_to_truly_start_adventure = "Press enter to truly start your adventure once and for all..."


you_encountered_a = "You encountered a "

you_find_yourself_staring_at_a_big_door = "You find yourself staring at a big door"

what_do_you_do = "What do you do?"

door_selections = "[1] - Knock on the door.\n" \
    "[2] - Try to open.\n"

you_knock_on_the_door = "You decided to knock on the door..."
nothing_is_happening = "After waiting for a moment you realise no one is coming..."


you_try_opening_door = "You decided to try to open the door..."

the_door_opened = "\n\n\nSuddenly the door opened!!"

and_out_came = "And before you could react, a knight stood upon you!"

knight_say_01 = "Woahhhhhhhhhh, Who are you? You shouldn't be here!"
knight_say_02 = "That seems familiar? Have we met before??"
knight_say_03 = "Doesn't matter, i've been instructed to eliminate all people i encounter!"


true_ident = "I think it's time that we discover your true identity and what you're really doing here..."
now_that_were_here = "Now that we're here..."

you_tried_opening_door = "\n\n\nYou decided it would be a good idea to open the door..."

after_trying = "\n\n\nAfter an amazing attempt on opening the door, you realise that if you just tried a little bit harder, \n it might just open.."

try_harder = "Try a little harder? [yes / no] "
you_tried_harder = "You tried a little bit harder to open the door"
then_it_opened = "when it magically swooshed open!"
you_decided_it_would_be_nicer_to_stay_here = "You eventually decided it would be nicer to stay here in this amazingly empty room with a door..."

dots = "..."

yes = "yes"
no = "no"

you_eventually_tried_opening = "You eventually tried opening the door out of boredom..."

battle_menu_selection = "[1] - Check Opponent.\n" \
                         "[2] - Attack.\n" \
                         "[3] - Talk to.\n"


def empty_list_placeholder(first, second, third):
    empty_list_placeholder = f"[1] - {first}\n" \
                            f"[2] - {second}\n" \
                            f"[3] - {third}\n"
    return empty_list_placeholder


name = "Name"
type = "Type"
level = "Level"