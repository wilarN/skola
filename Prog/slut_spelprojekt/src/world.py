import random
import time

import src.headers as headers
from src.misc import monster
import src.symbols as sym

global tiles_in_x
global tiles_in_y


class tile:
    def __init__(self, allow_entrance: bool, event, texture: str, x_location, y_location):
        self.allow_entrance = allow_entrance
        self.event = event
        self.texture = texture
        self.x_location = x_location
        self.y_location = y_location


def get_tile_information(tile_x, tile_y):
    global tiles_in_x
    global tiles_in_y
    tiles_in_x(tile_x)
    tiles_in_y(tile_y)


def introduction():
    headers.styled_coloured_print_centered(headers.lang.rules_and_introduction)
    headers.enter_to_continue()
    headers.clear()
    headers.space_down_three_new_lines()
    headers.styled_coloured_print_centered(headers.lang.are_you_ready_to_start)
    headers.space_down_three_new_lines()
    headers.styles_input(headers.lang.Press_enter_to_truly_start_adventure, True)
    headers.update_json_settings("Has_Begun", True)
    headers.clear()
    dummy_room()


def calculate_damage(ground_damage: int = 1):
    total_damage = round((headers.reverse_difficulty_number() / 10) * (random.randint(3, 7)) * ground_damage)
    # Instant kill for testing purposes (temporary)
    # total_damage = 100
    return total_damage


def flush():
    print("", flush=True)


def attack_countdown(opponent):
    opponent.say(headers.lang.npc_groan())
    time.sleep(headers.random.randint(3, 5))
    start = time.perf_counter()
    headers.styled_coloured_print_centered(text=sym.attack_indicator, colour="red", instant=True)
    while True:
        if headers.keyb.is_pressed("spacebar"):
            headers.styled_coloured_print_centered(text="\n*Dodge*\n", colour="blue", instant=True)
            finish = time.perf_counter()
            elapsed_time = finish - start
            if elapsed_time < headers.random.uniform(0.3, (headers.reverse_difficulty_number() / 10)):
                headers.styled_coloured_print_centered(text=f"{headers.lang.you_successfully} {headers.lang.dodged}.",
                                                       colour="orange")
                time.sleep(1)
                break
            else:
                headers.styled_coloured_print_centered(text=f"{headers.lang.you_failed_to} {headers.lang.dodge}.",
                                                       colour="red")
                dmg = calculate_damage()
                headers.styled_coloured_print_centered(text=f"{headers.lang.you_took} {dmg} {headers.lang.damage}.",
                                                       colour="orange")
                time.sleep(1)
                # headers.player.health -= dmg
                headers.damage_player(int(dmg))
                # headers.player.die()
                if headers.check_json_value_settings("player_health") <= 0:
                    headers.player.die()
                time.sleep(2)
                break


def what_do_you_want_to_do(corridor_things):
    what_choices = ["Look around", "Check inventory"]

    while True:
        tempNUM = 1
        for item in what_choices:
            headers.styled_coloured_print_centered(text=f"[{str(tempNUM)}] {item}", colour="blue", instant=False)
            tempNUM += 1

        headers.space_down_three_new_lines()
        headers.styled_coloured_print_centered(text="What do you want to do?", colour="orange")
        what_to_do_user_anw = headers.styles_input("\n>> ", centered=True)

        if what_to_do_user_anw.__contains__("1"):
            corridor_things.what_do_you_see()
            break
        elif what_to_do_user_anw.__contains__("2"):
            headers.check_inventory()
            time.sleep(1)
            headers.clear()
            headers.styled_coloured_print_centered(text="\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-", colour="pink", instant=True)
            headers.space_down_three_new_lines()
        else:
            pass


def what_do_you_want_to_do_universal(selections):
    while True:
        tempNUM = 1
        for item in selections:
            headers.styled_coloured_print_centered(text=f"[{str(tempNUM)}] {item}", colour="blue", instant=False)
            tempNUM += 1

        headers.space_down_three_new_lines()
        headers.styled_coloured_print_centered(text="What do you want to do?", colour="orange")
        what_to_do_user_anw = headers.styles_input("\n>> ", centered=True)

        if what_to_do_user_anw.__contains__("1"):
            return 1
        elif what_to_do_user_anw.__contains__("2"):
            return 2

        if len(selections) > 2:
            if len(selections) == 3:
                if what_to_do_user_anw.__contains__("3"):
                    return 3
                else:
                    pass
            elif len(selections) == 4:
                if what_to_do_user_anw.__contains__("4"):
                    return 4
                else:
                    pass
            else:
                pass
        else:
            pass
        headers.space_down_three_new_lines(True)


def defend_instructions():
    headers.styled_coloured_print_centered(text=headers.lang.defend_instructions, instant=True)
    time.sleep(2)
    headers.enter_to_continue()


def attack_npc(who_to_attack, portrate):
    headers.clear()
    headers.get_lines(text_obj=portrate, output=True, instant=True, colour="redpurple")
    if headers.check_json_value_settings("weapon_type") == "Default":
        # DEFAULT SLASH
        while True:
            headers.styled_coloured_print_centered(
                headers.lang.empty_list_placeholder("Unarmed Strike", "Slash", "Bonk"), "red")
            usr_sel = headers.styles_input("\n>> ", centered=True)
            if usr_sel.__contains__("1"):
                # Unarmed Strike
                dmg = calculate_damage(ground_damage=4)
                headers.styled_coloured_print_centered(
                    text=f"{headers.get_user_data(1)} {headers.lang.used} Unarmed Strike.", colour="orange")
                time.sleep(1)
                who_to_attack.damage(dmg)
                # print(who_to_attack.health)
                time.sleep(2)

                if not who_to_attack.is_alive():
                    who_to_attack.die()
                    break
                else:
                    if int(headers.check_json_value_settings("player_experience")) < 1:
                        defend_instructions()
                    headers.clear()
                    headers.get_lines(text_obj=portrate, output=True, instant=True, colour="purpleblue")
                    time.sleep(1)
                    headers.clear()
                    headers.get_lines(text_obj=portrate, output=True, instant=True)

                    headers.styled_coloured_print_centered(
                        f"{who_to_attack.name} {headers.lang.prepared_his_attack}...")
                    attack_countdown(who_to_attack)
                    headers.clear()
                    headers.get_lines(text_obj=portrate, output=True, instant=True, colour="purpleblue")
                    break

            elif usr_sel.__contains__("2"):
                # Slash
                dmg = calculate_damage(ground_damage=6)
                headers.styled_coloured_print_centered(
                    text=f"{headers.get_user_data(1)} {headers.lang.used} Slash.", colour="orange")
                time.sleep(1)
                who_to_attack.damage(dmg)
                # print(who_to_attack.health)
                time.sleep(2)

                if not who_to_attack.is_alive():
                    who_to_attack.die()
                    break
                else:
                    if int(headers.check_json_value_settings("player_experience")) < 1:
                        defend_instructions()
                    headers.clear()
                    headers.get_lines(text_obj=portrate, output=True, instant=True, colour="purpleblue")
                    time.sleep(1)
                    headers.clear()
                    headers.get_lines(text_obj=portrate, output=True, instant=True)

                    headers.styled_coloured_print_centered(
                        f"{who_to_attack.name} {headers.lang.prepared_his_attack}...")
                    attack_countdown(who_to_attack)
                    headers.clear()
                    headers.get_lines(text_obj=portrate, output=True, instant=True, colour="purpleblue")
                    break

            elif usr_sel.__contains__("3"):
                # Bonk
                dmg = calculate_damage(ground_damage=4)
                headers.styled_coloured_print_centered(
                    text=f"{headers.get_user_data(1)} {headers.lang.oddly_bonked}.", colour="orange")
                time.sleep(5)
                who_to_attack.damage(dmg)
                # print(who_to_attack.health)
                time.sleep(2)

                if not who_to_attack.is_alive():
                    who_to_attack.die()
                    break
                else:
                    if int(headers.check_json_value_settings("player_experience")) < 1:
                        defend_instructions()
                    headers.clear()
                    headers.get_lines(text_obj=portrate, output=True, instant=True, colour="purpleblue")
                    time.sleep(1)
                    headers.clear()
                    headers.get_lines(text_obj=portrate, output=True, instant=True)

                    headers.styled_coloured_print_centered(
                        f"{who_to_attack.name} {headers.lang.prepared_his_attack}...")
                    attack_countdown(who_to_attack)
                    headers.clear()
                    headers.get_lines(text_obj=portrate, output=True, instant=True, colour="purpleblue")
                    break

    # Enemy attack back.
    '''
    magic_wand = headers.summon_item("magic_wand", "Magic wand used for testing purposes")
    orb_of_fire = headers.summon_item("blue_fire_orb", "Item that's used for testing purposes")
    headers.backpackAddItem(magic_wand, 1)
    headers.backpackAddItem(orb_of_fire, 1)
    '''
    # print(headers.backpackGetAllItems())


def start_battle(who_you_fighting, battle_voice_lines=None, portrate=None):
    if portrate is not None:
        headers.clear()
        headers.get_lines(text_obj=portrate, output=True, instant=True, colour="redpurple")
    who_you_fighting.attack_vline()
    time.sleep(1)
    print("\n")
    headers.ps.Write.Print(
        text=headers.ps.Center.XCenter(f"--- | {headers.get_user_data(1)} vs {who_you_fighting.name} | ---\n\n"),
        color=headers.ps.Colors.blue_to_white, interval=0.0001)
    # who_you_fighting.set_voicelines(battle_voice_lines)
    # who_you_fighting.say_lines()
    while True:
        print("", flush=True)
        headers.styled_coloured_print_centered(text=headers.lang.battle_menu_selection)
        usr_answ = headers.styles_input("\n>> ", centered=True)
        if usr_answ.__contains__("1"):
            # Check opponent
            temp_num = 1
            for line in who_you_fighting.get_all_stats():
                if temp_num == 1:
                    print(headers.ps.Center.XCenter(f"{headers.lang.name}: {line}"), end="")
                elif temp_num == 2:
                    print(headers.ps.Center.XCenter(f"{headers.lang.type}: {line}"), end="")
                elif temp_num == 3:
                    print(headers.ps.Center.XCenter(f"{headers.lang.level}: {line}"), end="")
                if type(line) == int:
                    line = str(line)
                print("", flush=True)
                temp_num += 1

        elif usr_answ.__contains__("2"):
            # Attack
            attack_npc(who_to_attack=who_you_fighting, portrate=portrate)
        elif usr_answ.__contains__("3"):
            # Talks
            headers.clear()
            headers.get_lines(text_obj=portrate, output=True, instant=True, colour="purpleblue")
            print("", flush=True)
            temp_num = 1
            exit_num = 0
            for sel in who_you_fighting.talk_selections:
                headers.styled_coloured_print_centered(text=f"[{temp_num}] {sel}")
                temp_num += 1
            usr_answ = headers.styles_input("\n>> ", centered=True)
            if usr_answ.__contains__("1"):
                flush()
                line = who_you_fighting.user_talk_selections[0]
                headers.styled_coloured_print_centered(line)
                time.sleep(2)
                headers.ps.Write.Print(
                    text=headers.ps.Center.XCenter(f"*{who_you_fighting.name} {who_you_fighting.responses[0]}*"),
                    color=headers.ps.Colors.orange, interval=0.01)
                if "^" in who_you_fighting.responses[0]:
                    exit_num = 1
                time.sleep(1)
                headers.enter_to_continue()
                if exit_num == 1:
                    break
                if not who_you_fighting.alive:
                    break
            elif usr_answ.__contains__("2"):
                flush()
                line = who_you_fighting.user_talk_selections[1]
                headers.styled_coloured_print_centered(line)
                time.sleep(2)
                headers.ps.Write.Print(
                    text=headers.ps.Center.XCenter(f"*{who_you_fighting.name} {who_you_fighting.responses[1]}*"),
                    color=headers.ps.Colors.orange, interval=0.01)
                time.sleep(1)
                if "^" in who_you_fighting.responses[1]:
                    exit_num = 2
                    who_you_fighting.passBy()
                headers.enter_to_continue()
            # ENEMY ATTACK
            if who_you_fighting.alive:
                if int(headers.check_json_value_settings("player_experience")) < 1:
                    defend_instructions()
                headers.clear()
                headers.get_lines(text_obj=portrate, output=True, instant=True, colour="purpleblue")
                time.sleep(1)

                headers.styled_coloured_print_centered(f"{who_you_fighting.name} {headers.lang.prepared_his_attack}...")
                attack_countdown(who_you_fighting)
                headers.clear()
                headers.get_lines(text_obj=portrate, output=True, instant=True, colour="purpleblue")
            elif not who_you_fighting.alive:
                break
        else:
            pass
        # Exit battle system.
        if not who_you_fighting.alive:
            break

    # POINTS GRANT ITEMS ETC::: AFTER BATTLE IS FINISHED

    # Grant loot-->
    '''for loot in who_you_fighting.loot:
        headers.backpackAddItem(loot, 1)
        time.sleep(0.1)
    headers.grantXP((headers.random.randint(1, 5) * int(headers.check_json_value_settings("realm_difficulty"))))
    '''


def dummy_room():
    headers.update_json_settings("current_room_index", "1")

    rm = room(type=1)
    rm.get_monsters()
    rm.start()

    # Temp testing lines to skip to the good part and not have to go through the whole story and convo

    # dummy_knight = headers.misc.npc(alive=True, name="Carlos", level=1, type="knight",
    #                                 user_talk_selections=[headers.lang.usr_knight_line_sel_01_line,
    #                                                       headers.lang.usr_knight_line_sel_02_line],
    #                                 talk_selections=headers.lang.knight_talk_selection, status=None,
    #                                 char_sym=sym.knight_standing, attack_line=headers.lang.knight_attack_line,
    #                                 responses=[headers.lang.knight_reply_happy02,
    #                                            headers.lang.knight_reply_fight_end01], loot=[headers.items.magic_orb])
    # usr_said_name = "testName"
    # headers.clear()
    #
    # headers.get_lines(sym.knight_standing, True)
    # start_battle(who_you_fighting=dummy_knight, portrate=sym.knight_standing,
    #              battle_voice_lines=[headers.lang.now_that_were_here, headers.lang.true_ident])

    headers.styled_coloured_print_centered(headers.lang.woke_up)
    headers.styled_coloured_print_centered(headers.lang.not_knowing)
    headers.enter_to_continue()
    headers.clear()
    print("\n\n\n")
    headers.styled_coloured_print_centered(headers.lang.you_find_yourself_staring_at_a_big_door)
    print()
    time.sleep(1)
    # rm.print(headers.lang.what_do_you_do)
    headers.get_lines(text_obj=sym.door_closed, output=True, instant=True)
    while True:
        headers.styled_coloured_print_centered(headers.lang.door_selections)
        usr_sel = headers.styles_input("\n>> ", centered=True)
        if usr_sel.__contains__("1"):
            headers.clear()
            headers.get_lines(text_obj=sym.door_closed, output=True, instant=True)
            headers.styled_coloured_print_centered(headers.lang.you_knock_on_the_door)
            print("", flush=True)
            time.sleep(1)
            headers.styled_coloured_print_centered(headers.lang.nothing_is_happening)
            headers.enter_to_continue()
            headers.clear()
            headers.space_down_three_new_lines()
            headers.styled_coloured_print_centered(headers.lang.the_door_opened)
            headers.get_lines(text_obj=sym.door_open, output=True, instant=True)
            headers.styled_coloured_print_centered(headers.lang.and_out_came)

            break
        elif usr_sel.__contains__("2"):
            headers.clear()
            headers.space_down_three_new_lines()
            headers.styled_coloured_print_centered(headers.lang.you_tried_opening_door),
            headers.get_lines(text_obj=sym.door_closed, output=True, instant=True)
            time.sleep(1)
            while True:
                headers.space_down_three_new_lines()
                headers.styled_coloured_print_centered(headers.lang.after_trying)
                print("", flush=True)
                usr_sel = headers.styles_input(headers.lang.try_harder, centered=True)
                if usr_sel.lower() == headers.lang.yes:
                    headers.styled_coloured_print_centered(headers.lang.you_tried_harder)
                    print("", flush=True)
                    time.sleep(1)
                elif usr_sel.lower() == headers.lang.no:
                    headers.styled_coloured_print_centered(headers.lang.you_decided_it_would_be_nicer_to_stay_here)
                    time.sleep(1)
                    for i in range(0, 4):
                        print("", flush=True)
                        headers.styled_coloured_print_centered(headers.lang.dots)
                        time.sleep(1)
                    print("", flush=True)
                    headers.styled_coloured_print_centered(headers.lang.you_eventually_tried_opening)
                    time.sleep(1)
                    headers.enter_to_continue()
                headers.clear()
                headers.styled_coloured_print_centered(headers.lang.then_it_opened)
                headers.get_lines(text_obj=sym.door_open, output=True, instant=True)
                headers.styled_coloured_print_centered(headers.lang.and_out_came)
                break
            break
        else:
            pass

    headers.get_lines(text_obj=sym.knight_standing, output=True, instant=True)
    dummy_knight = headers.misc.npc(alive=True, name="Carlos", level=1, type="knight",
                                    user_talk_selections=[headers.lang.usr_knight_line_sel_01_line,
                                                          headers.lang.usr_knight_line_sel_02_line],
                                    talk_selections=headers.lang.knight_talk_selection, status=None,
                                    char_sym=sym.knight_standing, attack_line=headers.lang.knight_attack_line,
                                    responses=[headers.lang.knight_reply_happy02,
                                               headers.lang.knight_reply_fight_end01], loot=[headers.items.magic_orb])
    dummy_knight.say(headers.lang.knight_say_01)
    usr_said_name = headers.styles_input("\nYour name? >> ", centered=True)
    dummy_knight.set_voicelines(
        [f"{usr_said_name}....", headers.lang.knight_say_02, headers.lang.knight_say_03])
    dummy_knight.say_lines()
    headers.enter_to_continue()
    headers.clear()

    headers.get_lines(text_obj=sym.knight_standing, output=True, instant=True)
    start_battle(who_you_fighting=dummy_knight, portrate=sym.knight_standing,
                 battle_voice_lines=[headers.lang.now_that_were_here, headers.lang.true_ident])
    headers.update_json_settings("current_room_index", "2")


class corridor:
    def __init__(self, things_in_corridor: list = None, things_functions=None, enter_text: str = "Entered."):
        self.enter_text = enter_text
        self.things_in_corridor = things_in_corridor
        self.things_functions = things_functions

    def enter(self):
        headers.clear()
        headers.space_down_three_new_lines()
        headers.styled_coloured_print_centered(text=self.enter_text)
        time.sleep(2)
        headers.space_down_three_new_lines()

    def what_do_you_see(self):
        while True:
            headers.clear()
            headers.space_down_three_new_lines()
            headers.styled_coloured_print_centered(text="You notice a few things in your surrounding: ",
                                                   colour="orange", instant=True)
            headers.space_down_three_new_lines()
            tempNUM = 1
            for item in self.things_in_corridor:
                headers.styled_coloured_print_centered(text=f"[{str(tempNUM)}] {item}", colour="blue", instant=False)
                tempNUM += 1

            usr_sel = headers.styles_input("\n>> ", centered=True)
            if usr_sel.__contains__("1"):
                self.things_functions[0]()
                break
            elif usr_sel.__contains__("2"):
                self.things_functions[1]()
                break


def inspect(object_to_inspect):
    headers.styled_coloured_print_centered(text=object_to_inspect.description, colour="blue")
    headers.space_down_three_new_lines()
    headers.enter_to_continue()


def strange_door():
    headers.clear()
    headers.space_down_three_new_lines()
    headers.styled_coloured_print_centered(
        text="Upon walking up to the strange looking door, you start hearing a water-like noise coming from behind.")
    headers.space_down_three_new_lines()
    headers.enter_to_continue()
    headers.clear()
    headers.space_down_three_new_lines()
    headers.styled_coloured_print_centered(
        text="And before you could react you stood face to face with a medium sized slime!")
    headers.enter_to_continue()


def sticky_slime():
    headers.clear()
    headers.space_down_three_new_lines()
    headers.styled_coloured_print_centered("You walk to the oddly shaped puddle.")
    time.sleep(2)
    headers.styled_coloured_print_centered(
        "The puddle looks like something you would find in the trash can and that's been laying there for at least a few hundred years.")
    headers.space_down_three_new_lines()
    time.sleep(2)
    result = what_do_you_want_to_do_universal(["Touch the puddle.", "Stand in the puddle."])
    if result == 1:
        headers.clear()
        headers.space_down_three_new_lines()
        headers.styled_coloured_print_centered("You decided to gently touch the puddle.")
        time.sleep(2)
        headers.enter_to_continue()
        headers.clear()
        headers.styled_coloured_print_centered("Suddenly the puddle started to rise!")
        time.sleep(3)

    elif result == 2:
        headers.clear()
        headers.space_down_three_new_lines()
        headers.styled_coloured_print_centered("You decided to stand in the puddle.")
        time.sleep(2)
        headers.enter_to_continue()
        headers.clear()
        headers.styled_coloured_print_centered("And suddenly the puddle started to rise!")
        time.sleep(3)


class door:
    def __init__(self, opened):
        self.opened = opened

    def move_through(self):
        if self.opened:
            return True
        else:
            return False


class room:
    loot = []
    mobs = []

    def __init__(self, type):
        self.type = type
        self.room_index = headers.get_free_room_index() + 1
        if self.room_index not in headers.rooms:
            # Only add room if not exists.
            headers.rooms.append(self.room_index)
        else:
            pass

        if self.type == 1:
            # Standard Room
            self.get_monsters()
        elif self.type == 2:
            # No monster-filled room
            pass

        else:
            # Invalid Selection
            pass

    def get_loot_table(self):
        diff = headers.get_realm_data(3)
        player_lvl = headers.get_user_data(3)

    def get_monsters(self):
        diff = headers.get_realm_data(3)
        player_lvl = headers.get_user_data(3)
        for i in range(1, random.randint(1, 4)):
            self.mobs.append(monster(health=1 * diff, alive=True, level=player_lvl))

    def start(self):
        # print(f"Init room: {self.room_index}")
        pass

    def print(self, msg):
        headers.styled_coloured_print(msg)


def room01():
    headers.update_json_settings("current_room_index", "2")

    # Temp testing lines to skip to the good part and not have to go through the whole story and convo

    cor = corridor(enter_text="You entered a cold and wet corridor.",
                   things_in_corridor=["Strange door.", "Weird puddle of sticky residue?"],
                   things_functions=[strange_door, sticky_slime])

    cor.enter()
    what_do_you_want_to_do(cor)

    slime = headers.misc.npc(alive=True, name="Quibble", level=2, type="slime",
                             user_talk_selections=[
                                 "You asked the slime about the importance of slime in todays society..?",
                                 "You tried using a spoon to collect some of the slime residue..."],
                             talk_selections=["Importance of slime.", "Use a spoon."], status=None,
                             char_sym=sym.slime_01,
                             attack_line="squished itself against the floor making a quiet splash sound!",
                             responses=[
                                 "agreed that slime is important for the modern world, but a feeling told you it probably wasn't objective about it's opinion!",
                                 "made sure you got the perfect amount of slime(unknown residue) just to keep you curious about it's texture."],
                             loot=[headers.items.unknown_residue])
    headers.clear()

    headers.get_lines(text_obj=sym.slime_01, output=True, instant=True, colour="pink")
    start_battle(who_you_fighting=slime, portrate=sym.slime_01,
                 battle_voice_lines=["*Squibble squibble*", "*More squibble squibble but louder*"])

    # Locate First Chest
    firstChest = headers.misc.chest([headers.items.dream_shard, headers.items.old_rag],
                                    "A true old wooden chest.. Has certinly seen better days.")

    headers.clear()
    headers.space_down_three_new_lines()
    headers.styled_coloured_print_centered(
        text="In the end of the corridor you notice there's a chest or coffin of some sort.", colour="orange")
    time.sleep(1)
    headers.space_down_three_new_lines()
    headers.styled_coloured_print_centered(text="You decide to walk to the chest.", colour="orange")
    time.sleep(1)
    headers.enter_to_continue()
    while True:
        headers.clear()
        headers.space_down_three_new_lines()
        firstChest.chest_enter()
        question = what_do_you_want_to_do_universal(["Open the chest", "Inspect", "- Continue(Move on) -"])
        if question == 1:
            # Open chest
            headers.clear()
            if len(firstChest.items) > 0:
                firstChest.open()
            else:
                headers.space_down_three_new_lines()
                headers.styled_coloured_print_centered(
                    text="You tried opening the already opened chest? And you managed to do it!", colour="orange")
                headers.space_down_three_new_lines()
                headers.enter_to_continue()
        elif question == 2:
            # Inspect
            inspect(firstChest)
        elif question == 3:
            break

    headers.clear()
    headers.space_down_three_new_lines()
    headers.styled_coloured_print_centered(text="You move further down the corridor...")
    time.sleep(2)
    headers.space_down_three_new_lines(True)
    headers.styled_coloured_print_centered(text="You end up at a sign and two doors.")
    headers.enter_to_continue()
    headers.clear()
    headers.space_down_three_new_lines()
    headers.get_lines(text_obj=sym.two_doors, colour="purpleblue")
    headers.get_lines(text_obj=sym.sign_01, colour="orange")
    time.sleep(2)
    headers.styled_coloured_print_centered(text="On the sign you can read: ")
    headers.space_down_three_new_lines()
    headers.styled_coloured_print_centered(text="GO IN ONE DOOR, AND THE OTHER ONE SHALL DISAPPEAR.", colour="red")
    headers.space_down_three_new_lines()

    while True:
        question = what_do_you_want_to_do_universal(["Door to the left", "Door to the right"])
        if question == 1:
            # Left door
            room_01_left_selection(previous_selection=question)
            break
        elif question == 2:
            # Right door
            room_01_right_selection(previous_selection=question)
            break
        else:
            headers.clear()
            headers.space_down_three_new_lines()
            headers.get_lines(text_obj=sym.two_doors, colour="purpleblue")
            headers.get_lines(text_obj=sym.sign_01, colour="orange")
            pass


def room_01_left_selection(previous_selection, after: bool = False):
    headers.clear()
    headers.space_down_three_new_lines()
    if not after:
        headers.styled_coloured_print_centered(text="*You enter the door on the left*", colour="purpleblue")
        headers.styled_coloured_print_centered(text="- [PATH CHOSEN] -", colour="red")
    time.sleep(2)
    headers.clear()
    headers.space_down_three_new_lines()
    headers.styled_coloured_print_centered(text="Right when you entered the room,")
    time.sleep(1)
    headers.styled_coloured_print_centered(text="you were met with a strong flashing light instantly blinding you.")
    headers.get_lines(text_obj=sym.wall_of_souls, colour="greenwhite")
    headers.enter_to_continue()
    wall_of_souls = headers.misc.npc(alive=True, name="Wall Of Souls", level=2, type="Soul Eater",
                                     talk_selections=["Interests", "Blind back"], status=None, user_talk_selections=[
            "You tried asking the wall about it's interests.",
            "You used a small handheld mirror to reflect back the light!"],
                                     char_sym=sym.slime_01,
                                     attack_line="shines through you!",
                                     responses=["heard what you said, But still didn't seem amused!",
                                                "does not have eyes, which you soon enough realised..."],
                                     loot=[headers.items.green_lantern_of_eternal_souls])
    start_battle(who_you_fighting=wall_of_souls, portrate=sym.wall_of_souls,
                 battle_voice_lines=["*A strange light filled the room*", "*Green light shall shine through you*"])

    if previous_selection == 1:
        room_01_right_selection(previous_selection=previous_selection, after=True)
    headers.update_json_settings("current_room_index", "3")


def room_01_right_selection(previous_selection, after: bool = False):
    headers.clear()
    headers.space_down_three_new_lines()
    if not after:
        headers.styled_coloured_print_centered(text="*You enter the door on the right*", colour="purpleblue")
        headers.styled_coloured_print_centered(text="- [PATH CHOSEN] -", colour="red")
    time.sleep(2)
    headers.clear()
    headers.space_down_three_new_lines()
    headers.styled_coloured_print_centered(text="Right when you entered the room,", colour="greenyellow")
    time.sleep(1)
    headers.get_lines(text_obj=sym.sign_01, colour="orange")
    time.sleep(1)
    headers.styled_coloured_print_centered(text="you were met with another sign, reading:", colour="greenyellow")
    headers.space_down_three_new_lines()
    headers.styled_coloured_print_centered(
        text='"RIGHT IS NOT ALWAYS RIGHT, BUT LEFT ALMOST ALWAYS CERTAINLY IS NOT THE RIGHT ONE."', colour="red")
    time.sleep(2)
    headers.styled_coloured_print_centered(text="You think about it for a second.", colour="greenyellow")
    headers.space_down_three_new_lines(single=True)
    headers.styled_coloured_print_centered(text="Reading it over and over, but it still don't make any sense.",
                                           colour="greenyellow")

    # Sign
    sign_mimic = headers.misc.npc(alive=True, name="Sign Mimic", level=3, type="Mimic",
                                  talk_selections=["Compliment", "Scare"], status=None,
                                  user_talk_selections=[
                                      "You told the sign it looked well polished.",
                                      "You tried scaring the sign with a lighter!"],
                                  char_sym=sym.sign_mimic01,
                                  attack_line="shines through you!",
                                  responses=["heard what you said, But still didn't seem amused!",
                                             "jumped back a meter trying to avoid the massive(not so massive) flames.."],
                                  loot=[headers.items.mimic_mage_scroll])

    while True:
        headers.space_down_three_new_lines()
        sel = what_do_you_want_to_do_universal(["Move on", "Read again (Might be worth a second try!)"])
        if sel == 1:
            # Move on.
            headers.styled_coloured_print_centered(
                "You decided the sign has already simply wasted your valuable time and it is time to move on.",
                colour="greenyellow")
            time.sleep(1)
            headers.enter_to_continue()
            headers.styled_coloured_print_centered(
                text="But upon leaving the sign, you hear something crackling behind you.", colour="greenyellow")
            time.sleep(1)
            headers.styled_coloured_print_centered(
                text="When you turned around to see what was there, you stood eye to eye with a sign monster.",
                colour="greenyellow")
            headers.enter_to_continue()
            headers.clear()
            headers.space_down_three_new_lines()
            headers.styled_coloured_print_centered(
                text="You've read from books that these creatures are so called mimics. Who usually take the form of chests or even signs.",
                colour="greenyellow")
            headers.enter_to_continue()
            break
        elif sel == 2:
            # Read again.
            headers.styled_coloured_print_centered(text="You read the sign again.", colour="greenyellow")
            time.sleep(1)
            headers.space_down_three_new_lines()
            headers.styled_coloured_print_centered(
                text="Upon reading the sign a second time, you noticed something new.", colour="greenyellow")
            time.sleep(1)
            headers.space_down_three_new_lines()
            headers.styled_coloured_print_centered(text="There was something strange about this particular sign.",
                                                   colour="greenyellow")
            time.sleep(1)
            headers.space_down_three_new_lines()
            headers.styled_coloured_print_centered(
                text="You notice there is some white fur stuck in the upper right corner of the sign.",
                colour="greenyellow")
            headers.space_down_three_new_lines()

            # Touch the fur?
            while True:
                sel = what_do_you_want_to_do_universal(["Touch the fur.", "Leave the fur alone."])
                if sel == 1:
                    # Touch the fur.
                    headers.styled_coloured_print_centered(
                        "You touch the fur.")
                    headers.enter_to_continue()
                    break
                elif sel == 2:
                    # Don't touch the fur.
                    headers.styled_coloured_print_centered(
                        "You decided the sign has already simply wasted your valuable time enough and it is time to move on.")
                    time.sleep(1)
                    headers.enter_to_continue()
                    headers.styled_coloured_print_centered(
                        text="But upon leaving the sign, you hear something crackling behind you.",
                        colour="greenyellow")
                    time.sleep(1)
                    headers.styled_coloured_print_centered(
                        text="When you turned around to see what was there, you stood eye to eye with a sign monster.",
                        colour="greenyellow")
                    headers.enter_to_continue()
                    headers.clear()
                    headers.space_down_three_new_lines()
                    headers.styled_coloured_print_centered(
                        text="You've read from books that these creatures are so called mimics. Who usually take the form of chests or even signs.",
                        colour="greenyellow")
                    headers.enter_to_continue()
                    break
            break
        else:
            pass

    headers.clear()
    headers.space_down_three_new_lines()

    sign_mimic.portrait()
    sign_mimic.say("This sign! Will some day rule the world!! hAhA")
    sign_mimic.set_voicelines(["Although, that day might not be today..",
                               "But for now! I will fight you until the end, even if it means shedding blood.",
                               "Brace yourself, human."])
    sign_mimic.say_lines()
    headers.space_down_three_new_lines()

    headers.enter_to_continue()

    start_battle(who_you_fighting=sign_mimic, portrate=sign_mimic.char_sym,
                 battle_voice_lines=[
                     "The sign mimic braced itself by carving out a little knife from itself.",
                     "Its time."])
    if previous_selection == 2:
        room_01_left_selection(previous_selection=previous_selection, after=True)

    headers.update_json_settings("current_room_index", "3")


def the_end_room():
    # Final room.
    headers.clear()
    headers.styled_coloured_print_centered(text="-+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-\n"
                                                "+                                                    + \n"
                                                "-           Thanks for playing AURORA DEMO.          - \n"
                                                "+                  William Johnsson.                 + \n"
                                                "-                                                    - \n"
                                                "+                                                    + \n"
                                                "+                                                    + \n"
                                                "-    This version was far from finished!             - \n"
                                                "+    But I hope you enjoyed the short demo version.  + \n"
                                                "-                                                    - \n"
                                                "+                                                    + \n"
                                                "-    If you feel like starting over, just delete     - \n"
                                                "-    the settings.json file and re-run the aurora.py - \n"
                                                "-                                                    - \n"
                                                "+                                                    + \n"
                                                "+           [   THANKS FOR PLAYING! <3   ]           + \n"
                                                "-                                                    - \n"
                                                "+                                                    + \n"
                                                "+    More updates will be posted on my github!       + \n"
                                                "-                                                    - \n"
                                                "+         @wilarN | @william.jsson@hotmail.com       + \n"
                                                "-              Discord: william_#6737                - \n" 
                                                "-+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-\n"
                                                "", instant=True, colour="greenwhite")
    headers.space_down_three_new_lines()
    headers.enter_to_continue()
    headers.clear()
    headers.space_down_three_new_lines()
    headers.styled_coloured_print_centered(text=sym.planet, instant=True, colour="purpleblue")
    headers.space_down_three_new_lines()
    headers.styled_coloured_print_centered(text="- A game made by William. J", colour="yellow", instant=False)
    time.sleep(2)
    exit(0)


# OBS, IMPORTANT ROOM ORDER BY INDEX!!
loaded_rooms_indexed = {
    "1": dummy_room,
    "2": room01,
    "3": the_end_room
}


class realm:
    def __init__(self, realm_name, realm_difficulty):
        self.realm_name = realm_name
        self.realm_difficulty = realm_difficulty
        self.last_known_player_pos_X = 0
        self.last_known_player_pos_Y = 0

    def map_gen(self, size_x, size_y):
        arr = [[0 for i in range(size_x)] for j in range(size_y)]
        arr[0][0] = 1
        # new_tile = tile(allow_entrance=True, x_location=i, y_location=j, texture="[x]", event=False)
        for row in arr:
            print(row)

    def generate_map(self, size_x, size_y):
        global tiles_in_x
        global tiles_in_y
        tiles_in_x = []
        tiles_in_y = []

        max_map_x = [x for x in range(1, size_x)]
        max_map_y = [x for x in range(1, size_y)]

        # tile = "[x]"
        # new_tile = tile(allow_entrance=True, event=False, texture="[x]")

        for tilex in max_map_x:
            # tiles_in_x.append(tile)
            tiles_in_x.append(
                tile(allow_entrance=True, event=False, texture="[y]", x_location=tilex, y_location=tilex))
            if len(tiles_in_x) <= 10:
                if len(tiles_in_x) > 0:
                    print(tiles_in_x[tilex - 1].texture)
                for tiley in max_map_y:
                    # tiles_in_y.append(tile)
                    tiles_in_y.append(
                        tile(allow_entrance=True, event=False, texture="[x]", x_location=tilex, y_location=tiley))
                    if len(tiles_in_y) > 0:
                        print(tiles_in_y[tiley - 1].texture, end="")

            else:
                tiles_in_x.clear()
                tiles_in_y.clear()

    def room_containing_npc(self):
        pass

    def room_static(self):
        print("Welcome to the static room.")
