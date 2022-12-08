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
    headers.styled_coloured_print_centered("\n\n\n" + headers.lang.are_you_ready_to_start)
    headers.styles_input(headers.lang.Press_enter_to_truly_start_adventure, True)
    headers.update_json_settings("Has_Begun", True)
    headers.clear()
    dummy_room()


def flush():
    print("", flush=True)


def attack_countdown(opponent):
    opponent.say(headers.lang.npc_groan())
    time.sleep(headers.random.randint(3, 5))
    start = time.perf_counter()
    headers.styled_coloured_print_centered(text=sym.attack_indicator, colour="red", instant=True)
    while True:
        if headers.keyb.is_pressed("spacebar"):
            print("*Dodge*")
            finish = time.perf_counter()
            elapsed_time = finish - start
            if elapsed_time > headers.random.uniform(0.3, (headers.reverse_difficulty_number() / 10)):
                return False
            else:
                return True


def defend_instructions():
    headers.styled_coloured_print_centered(headers.lang.defend_instructions)
    time.sleep(2)
    headers.enter_to_continue()


def attack_npc(who_to_attack, portrate):

    while True:
        headers.clear()
        headers.get_lines(text_obj=portrate, output=True, instant=True)
        headers.styled_coloured_print_centered(headers.lang.empty_list_placeholder("Badoink", "Smonk", "Bonk"), "red")
        usr_sel = headers.styles_input("\n>> ", centered=True)
        if usr_sel == "1":



    who_to_attack.say(headers.lang.we_will_meet_again)
    who_to_attack.set_voicelines([headers.lang.i_wont_forget_your_face])
    who_to_attack.say_lines()
    '''
    magic_wand = headers.summon_item("magic_wand", "Magic wand used for testing purposes")
    orb_of_fire = headers.summon_item("blue_fire_orb", "Item thats used for testing purposes")
    headers.backpackAddItem(magic_wand, 1)
    headers.backpackAddItem(orb_of_fire, 1)
    '''
    # print(headers.backpackGetAllItems())


def start_battle(who_you_fighting, battle_voice_lines, portrate=None):
    if portrate is not None:
        headers.clear()
        headers.get_lines(portrate, True, True)
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
        if usr_answ == "1":
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

        elif usr_answ == "2":
            # Attack
            attack_npc(who_to_attack=who_you_fighting, portrate=portrate)
        elif usr_answ == "3":
            # Talks
            headers.clear()
            headers.get_lines(portrate, True, True)
            print("", flush=True)
            temp_num = 1
            exit_num = 0
            for sel in who_you_fighting.talk_selections:
                headers.styled_coloured_print_centered(text=(f"[{temp_num}] {sel}"))
                temp_num += 1
            usr_answ = headers.styles_input("\n>> ", centered=True)
            if usr_answ == "1":
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
            elif usr_answ == "2":
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
                headers.enter_to_continue()
                if exit_num == 2:
                    break

            # ENEMY ATTACK
            if int(headers.check_json_value_settings("player_experience")) < 1:
                defend_instructions()
            headers.clear()
            headers.get_lines(portrate, True, True)
            time.sleep(1)

            headers.styled_coloured_print_centered(f"{who_you_fighting.name} {headers.lang.prepared_his_attack}...")
            att = attack_countdown(who_you_fighting)

        else:
            pass

    # POINTS GRANT ITEMS ETC::: AFTER BATTLE IS FINISHED

    # Grant loot-->
    for loot in who_you_fighting.loot:
        headers.backpackAddItem(loot, 1)
        time.sleep(0.1)
    headers.grantXP((headers.random.randint(1, 5) * int(headers.check_json_value_settings("realm_difficulty"))))


def dummy_room():
    rm = room(type=1)
    rm.get_monsters()
    rm.start()

    # Temp testing lines to skip to the good part and not have to go through the whole story and convo
    dummy_knight = headers.misc.npc(alive=True, name="Carlos", level=1, type="knight",
                                    user_talk_selections=[headers.lang.usr_knight_line_sel_01_line,
                                                          headers.lang.usr_knight_line_sel_02_line],
                                    talk_selections=headers.lang.knight_talk_selection, status=None,
                                    char_sym=sym.knight_standing, attack_line=headers.lang.knight_attack_line,
                                    responses=[headers.lang.knight_reply_happy02,
                                               headers.lang.knight_reply_fight_end01], loot=[headers.items.magic_orb])
    usr_said_name = "testName"
    headers.clear()

    headers.get_lines(sym.knight_standing, True)
    start_battle(who_you_fighting=dummy_knight, portrate=sym.knight_standing,
                 battle_voice_lines=[headers.lang.now_that_were_here, headers.lang.true_ident])

    headers.styled_coloured_print_centered(headers.lang.woke_up)
    time.sleep(1)
    headers.styled_coloured_print_centered(headers.lang.not_knowing + "\n\n\n")
    headers.enter_to_continue()
    headers.clear()
    headers.styled_coloured_print_centered("\n\n\n" + headers.lang.you_find_yourself_staring_at_a_big_door)
    print()
    time.sleep(1)
    # rm.print(headers.lang.what_do_you_do)

    headers.get_lines(sym.door_closed, True)
    while True:
        headers.styled_coloured_print_centered(headers.lang.door_selections)
        usr_sel = headers.styles_input("\n>> ", centered=True)
        if usr_sel.lower() == "1":
            headers.clear()
            headers.get_lines(sym.door_closed, True)
            headers.styled_coloured_print_centered(headers.lang.you_knock_on_the_door)
            print("", flush=True)
            time.sleep(1)
            headers.styled_coloured_print_centered(headers.lang.nothing_is_happening)
            headers.enter_to_continue()
            headers.clear()
            headers.styled_coloured_print_centered(headers.lang.the_door_opened)
            headers.get_lines(sym.door_open, True)
            headers.styled_coloured_print_centered(headers.lang.and_out_came)

            break
        elif usr_sel.lower() == "2":
            headers.clear()
            headers.styled_coloured_print_centered(headers.lang.you_tried_opening_door),
            headers.get_lines(sym.door_closed, True)
            time.sleep(1)
            while True:
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
                headers.get_lines(sym.door_open, True)
                headers.styled_coloured_print_centered(headers.lang.and_out_came)
                break
            break
        else:
            pass

    headers.get_lines(sym.knight_standing, True)
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

    headers.get_lines(sym.knight_standing, True)
    start_battle(who_you_fighting=dummy_knight, portrate=sym.knight_standing,
                 battle_voice_lines=[headers.lang.now_that_were_here, headers.lang.true_ident])


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
        print(f"Init room: {self.room_index}")

    def print(self, msg):
        headers.styled_coloured_print(msg)


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
