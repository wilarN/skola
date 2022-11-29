import pystyle as ps
class player:
    def __init__(self, name, health, mana, level, experience, status, alive, current_room_index):
        self.name = name
        self.current_room_index = current_room_index
        self.health = health
        self.mana = mana
        self.level = level
        self.experience = experience
        self.status = status
        self.alive = alive

    def get_all_stats(self):
        all_stats = [self.name, self.health, self.mana, self.level, self.experience, self.status, self.alive,
                     self.current_room_index]
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
    def __init__(self, name, level, type, status, alive):
        self.name = name
        self.race = level
        self.type = type
        self.status = status
        self.alive = alive

    def set_voicelines(self, lines):
        if len(lines) > 1:
            for line in lines:
                self.voicelines.append(line)

    def say(self, msg):
        # print(ps.Write.Print(color=ps.Colors.cyan, text=self.name), end="")
        ps.Write.Print(text=ps.Center.XCenter(f"[{self.name}] - {msg}"), color=ps.Colors.pink, interval=0.001)
        print("", flush=True)

    def say_lines(self):
        for line in self.voicelines:
            ps.Write.Print(text=ps.Center.XCenter(f"{line}"), color=ps.Colors.pink, interval=0.001)
            print("\n", flush=True)
