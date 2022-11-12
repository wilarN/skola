
class player:
    def __init__(self, name, mana, level, experience, status, alive):
        self.name = name
        self.mana = mana
        self.level = level
        self.experience = experience
        self.status = status
        self.alive = alive

    def get_all_stats(self):
        all_stats = [self.name, self.mana, self.level, self.experience, self.status, self.alive]
        return all_stats

    def get_stat_by_name(self, spec_stat):
        pass


class npc:
    def __init__(self, name, level, experience, type, status, alive):
        self.name = name
        self.race = level
        self.type = type
        self.experience = experience
        self.status = status
        self.alive = alive
