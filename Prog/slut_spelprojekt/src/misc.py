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
        if self.health <= 0:
            self.alive = False

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
                 attack_line=None, responses=None, char_sym=None, loot=None, health=100):
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
        pass

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
        headers.styled_coloured_print_centered(text=f"{self.name} {headers.lang.took} --> {damage} {headers.lang.damage}", colour="red")
        self.health += damage
