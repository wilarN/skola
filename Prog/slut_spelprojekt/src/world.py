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
    headers.styled_coloured_print_centered("\n\n\n"+headers.lang.are_you_ready_to_start)
    headers.styles_input(headers.lang.Press_enter_to_truly_start_adventure)
    headers.update_json_settings("Has_Begun", True)
    headers.clear()
    dummy_room()


def dummy_room():
    rm = room(type=1)
    rm.get_monsters()
    rm.start()
    headers.styled_coloured_print_centered(headers.lang.you_find_yourself_staring_at_a_big_door)
    print()
    time.sleep(1)
    # rm.print(headers.lang.what_do_you_do)

    headers.get_lines(sym.door_closed, True)
    while True:
        headers.styled_coloured_print_centered(headers.lang.door_selections)
        usr_sel = headers.styles_input("\n>> ", centered=False)
        if usr_sel.lower() == "1":
            headers.clear()
            headers.get_lines(sym.door_closed, True)
            headers.styled_coloured_print_centered(headers.lang.you_knock_on_the_door)
            print("", flush=True)
            time.sleep(2)
            headers.styled_coloured_print_centered(headers.lang.nothing_is_happening)
            time.sleep(2)
            headers.clear()
            headers.styled_coloured_print_centered(headers.lang.the_door_opened)
            headers.get_lines(sym.door_open, True)
            headers.styled_coloured_print_centered(headers.lang.and_out_came)
            headers.get_lines(sym.knight_standing, True)
            print("", flush=True)



            break
        elif usr_sel.lower() == "2":
            headers.styled_coloured_print(headers.lang.you_knock_on_the_door)
            break
        else:
            pass

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
