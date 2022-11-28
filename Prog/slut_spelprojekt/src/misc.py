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
    def __init__(self, name, level, experience, type, status, alive):
        self.name = name
        self.race = level
        self.type = type
        self.experience = experience
        self.status = status
        self.alive = alive
