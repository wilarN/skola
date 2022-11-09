
class player:
    def __init__(self, name, mana, level, experience, status, alive):
        self.name = name
        self.age = mana
        self.race = level
        self.experience = experience
        self.status = status
        self.alive = alive


class npc:
    def __init__(self, name, level, experience, type, status, alive):
        self.name = name
        self.race = level
        self.type = type
        self.experience = experience
        self.status = status
        self.alive = alive
