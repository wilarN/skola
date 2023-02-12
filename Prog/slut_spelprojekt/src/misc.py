import pystyle as ps
import time
import src.symbols as sym
import src.headers as headers


class player:
    def __init__(self, name, health, mana, level, experience, status, alive, current_room_index, backpack, weapon_type):
        self.name = name
        self.current_room_index = current_room_index
        self.health = health
        self.mana = mana
        self.level = level
        self.experience = experience
        self.status = status
        self.alive = alive
        self.backpack = backpack
        self.weapon_type = weapon_type

    def get_all_stats(self):
        all_stats = [self.name, self.health, self.mana, self.level, self.experience, self.status, self.alive,
                     self.current_room_index, self.backpack]
        return all_stats

    def die(self):
        headers.clear()
        headers.update_json_settings("player_health", 0)
        headers.space_down_three_new_lines()
        headers.styled_coloured_print_centered("You have died.", colour="red", instant=False)
        headers.space_down_three_new_lines()
        headers.styled_coloured_print_centered(
            "The game will now close, If you think you have what it takes to continue, please start it again.",
            colour="red", instant=False)
        time.sleep(5)
        exit(0)

    def heal(self, amount):
        self.health += amount

    def damage(self, amount):
        self.health -= amount


class monster:
    loot = []

    def __init__(self, health, level, alive=True):
        self.health = health
        self.level = level
        self.alive = alive

    def die(self):
        if self.health <= 0:
            self.alive = False

    def heal(self, amount):
        self.health += amount

    def damage(self, amount):
        self.health -= amount


class npc:
    voicelines = []

    # There are two types of ´responses´: Happy reply == Means you said the right thing, // Anger reply == Means you did not pick the right line.
    # Chosen by index
    def __init__(self, name, level, type, status, alive, user_talk_selections=None, talk_selections=None,
                 attack_line=None, responses=None, char_sym=None, loot=None, health=30):
        self.name = name
        self.level = level
        self.type = type
        self.status = status
        self.alive = alive
        self.char_sym = char_sym
        self.responses = responses
        self.attack_line = attack_line
        self.talk_selections = talk_selections
        self.user_talk_selections = user_talk_selections
        self.loot = loot
        self.health = health

    def get_all_stats(self):
        all_stats = [self.name, self.type, self.level]
        return all_stats

    def set_voicelines(self, lines):
        self.voicelines.clear()
        print("", flush=True)
        if len(lines) > 0:
            for line in lines:
                self.voicelines.append(line)

    def portrait(self):
        headers.get_lines(text_obj=self.char_sym, output=True, instant=True)

    def attack_vline(self):
        '''
        name of npc is already stated
        '''
        ps.Write.Print(text=ps.Center.XCenter(f"*{self.name} {self.attack_line}*"), color=ps.Colors.orange,
                       interval=0.01)
        print("", flush=True)

    def say(self, msg):
        # print(ps.Write.Print(color=ps.Colors.cyan, text=self.name), end="")
        ps.Write.Print(text=ps.Center.XCenter(f"[{self.name}] - {msg}"), color=ps.Colors.pink, interval=0.01)
        print("", flush=True)

    def say_lines(self):
        for line in self.voicelines:
            ps.Write.Print(text=ps.Center.XCenter(f"- {line}"), color=ps.Colors.pink, interval=0.01)
            print("\n", flush=True)
            time.sleep(0.5)
        time.sleep(2)

    def damage(self, damage):
        if self.health <= 0:
            self.die()
        headers.styled_coloured_print_centered(
            text=f"{self.name} {headers.lang.took} --> {damage} {headers.lang.damage}", colour="red")
        self.health -= damage

    def is_alive(self):
        if self.health <= 0:
            return False
        else:
            return True

    def die(self):
        headers.styled_coloured_print_centered(text=f"{headers.lang.you_defeated} {self.name}!")
        if len(self.loot) > 0:
            for item in self.loot:
                headers.backpackAddItem(item, 1)
                headers.grantXP(headers.random.randint(5, 40))
        self.alive = False
        headers.space_down_three_new_lines()
        headers.enter_to_continue()

    def passBy(self):
        headers.grantXP(headers.random.randint(5, 40))
        self.alive = False


class chest:
    def __init__(self, items, description: str = "This item does not have a description."):
        self.slots = 5
        self.items = items
        self.has_been_opened = False
        self.description = description

    def open(self):
        if len(self.items) > 0:
            while len(self.items) > 0:
                headers.clear()
                headers.space_down_three_new_lines()
                headers.get_lines(text_obj=headers.world.sym.chest01, colour="purpleblue")
                tempNUM = 1
                headers.styled_coloured_print_centered(text=f"- [ Old wooden chest ] -", colour="pink")
                headers.styled_coloured_print_centered(text="\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-", colour="purpleblue",
                                                       instant=True)
                headers.space_down_three_new_lines()
                for item in self.items:
                    headers.styled_coloured_print_centered(f"[{tempNUM}] - {item.name}")
                    tempNUM += 1

                headers.styled_coloured_print_centered(text="\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-", colour="purpleblue",
                                                       instant=True)
                while True:
                    headers.space_down_three_new_lines()
                    headers.styled_coloured_print_centered(text="Take item?(Write index of item):", colour="red")
                    what_to_do_user_anw = headers.styles_input("\n>> ", centered=True)
                    if what_to_do_user_anw.__contains__("1"):
                        headers.backpackAddItem(self.items[0], 1, True)
                        self.items.pop(0)
                        time.sleep(2)
                        headers.clear()
                        break
                    elif what_to_do_user_anw.__contains__("2"):
                        try:
                            headers.backpackAddItem(self.items[1], 1, True)
                            self.items.pop(1)
                        except:
                            break
                        time.sleep(2)
                        headers.clear()
                        break
                    else:
                        pass
        else:
            headers.styled_coloured_print_centered(text="This chest is empty.", colour="red")

    def chest_enter(self):
        headers.clear()
        headers.space_down_three_new_lines()
        headers.get_lines(text_obj=headers.world.sym.chest01, colour="purpleblue")

    def desc(self):
        headers.styled_coloured_print_centered(text=self.description, colour="blue")
