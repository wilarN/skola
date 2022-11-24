
class player:
    def __init__(self, name, health, mana, level, experience, status, alive):
        self.name = name
        self.health = health
        self.mana = mana
        self.level = level
        self.experience = experience
        self.status = status
        self.alive = alive

    def get_all_stats(self):
        all_stats = [self.name, self.health, self.mana, self.level, self.experience, self.status, self.alive]
        return all_stats


class npc:
    def __init__(self, name, level, experience, type, status, alive):
        self.name = name
        self.race = level
        self.type = type
        self.experience = experience
        self.status = status
        self.alive = alive
