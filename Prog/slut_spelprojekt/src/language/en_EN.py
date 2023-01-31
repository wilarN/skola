import time
from time import sleep
import random

'''
In user selection cases the "^" symbol represents the correct one to exit battle and win...
(Just dont tell anyone)
'''

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
not_knowing = "Not knowing where you were..."

create_realm_text = "Now, let's move on to creating the realm."

begin_welcome = "Welcome"

welcome_back = "Welcome back"
welcome_back_2 = "to"

begin_welcome_first_time = f"Welcome to AURORA. Now that you're ready for your adventure. Let's first start off with a few rules and goals."

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

the_door_opened = "Suddenly the door opened!!"

and_out_came = "And before you could react, a knight stood upon you!"

#########  KNIGHT ##########
knight_say_01 = "Woahhhhhhhhhh, Who are you? You shouldn't be here!"
knight_say_02 = "That seems familiar? Have we met before??"
knight_say_03 = "Doesn't matter, i've been instructed to eliminate all people i encounter!"

true_ident = "I think it's time that we discover your true identity and what you're really doing here..."
now_that_were_here = "Now that we're here..."
we_will_meet_again = "We will meet again..."
i_wont_forget_your_face = "And I'll never forget your face..."

knight_attack_line = "stumbled forward in pride expecting anyone around to cheer... (But you were the only one there)"
knight_talk_selection = ["Compliment.", "Act."]

usr_knight_line_sel_02_line = "Even though you find yourself inside, you somehow are able to scrape out a snowball from the wall and you throw it at the knight."
usr_knight_line_sel_01_line = "You told the knight you really liked his armour."
knight_reply_happy02 = "giggled behind the mask and even though you couldn't see him, an imaginary ghost told you he was probably smiling."
knight_reply_fight_end01 = "was extremely surprised by your snowball scraping skills. He tried doing the same thing, but failed miserably..."
# ^ CHAR TO END BATTLE IN A FRIENDLY MANNER

#################################

def talk_menu(npc_name):
    if npc_name == "knight":
        return knight_talk_selection


you_tried_opening_door = "You decided it would be a good idea to open the door..."

after_trying = "After an amazing attempt on opening the door, you realise that if you just tried a little bit harder, \n it might just open.."

try_harder = "Try a little harder? [yes / no] "
you_tried_harder = "You tried a little bit harder to open the door"
then_it_opened = "when it magically swooshed open!"
you_decided_it_would_be_nicer_to_stay_here = "You eventually decided it would be nicer to stay here in this amazingly empty room with a door..."

dots = "..."

yes = "yes"
no = "no"

you_eventually_tried_opening = "You eventually tried opening the door out of boredom..."

battle_menu_selection = "[1] - Check.\n" \
                        "[2] - Attack.\n" \
                        "[3] - Talk.\n"


def empty_list_placeholder(first, second, third, heading=None):
    if heading is None:
        empty_list_placeholder = f"[1] - {first}\n" \
                                 f"[2] - {second}\n" \
                                 f"[3] - {third}\n"
    else:
        empty_list_placeholder = f" -- {heading} -- " \
                                 f"[1] - {first}\n" \
                                 f"[2] - {second}\n" \
                                 f"[3] - {third}\n"

    return empty_list_placeholder


name = "Name"
type = "Type"
level = "Level"

Item_rewarded = "You got rewarded"
Experience_earned = "You earned"
Experience = "experience"

defend_instructions = "\n-- How to defend --\n" \
                      "[*] - When the indicator comes up on the screen, Press 'spacebar' on your keyboard as fast as you can.\n" \
                      "[*] - If you are fast enough, you may be able to DODGE!\n" \
                      "[*] - If not, you take damage and if you take repeated strikes or hits, you die.\n" \
                      "[*] - If your HP reaches 0, it's GAME OVER...\n" \
                      "[*] - The attack indicator is as shown below... When this pops up, dodge.\n\n" \
                      "  .\|/.\n" \
                      " (\   /) \n" \
                      " - -O- -\n" \
                      " (/   \)\n" \
                      " ,'/||'."

prepared_his_attack = "prepared his attack"
prepared_her_attack = "prepared her attack"
prepared_its_attack = "prepared its attack"


def npc_groan():
    groans = ["Arghhh", "Ahhhh", "Ouuughh"]
    return groans[random.randint(0, len(groans) - 1)]


swung_his_sword = "swung his sword.."

attacked = "attacked"
damage = "damage"
forr = "for"
used = "used"

took = "took"

you_successfully = "You successfully"
you_failed_to = "You failed to"
dodge = "dodge"
dodged = "dodged"

you_took = "You took"

oddly_bonked = "oddly bonked the ememy??? No one really knows what this means, but it seems to be working!."

you_defeated = "You defeated"

and_got = "and got"