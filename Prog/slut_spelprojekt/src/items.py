
class item:
    def __init__(self, name, description = "This item doesn't have a description.", consumed = False):
        self.name = name
        self.description = description


class magic_orb(item):
    def __init__(self, colour, name, description):
        super().__init__(name, description)
        self.colour = colour
        self.name = name
        self.description = description


magic_orb = magic_orb(name="Magic Orb", description="Magic orb that can glow in multiple different colours such as yellow, red and blue.. Is also controlled by voice commands.", colour="Blue")


unknown_residue = item(name="Unknown residue", description="Origin unknown.")
diamond_sword = item(name="Diamond Sword", description="A certified classic.")
dream_shard = item(name="Dream Shard", description="A purple shard containing high levels of dark energy.")
old_rag = item(name="Old Rag", description="An old multipurpose rag of some kind. Seems to badly damaged.")
green_lantern_of_eternal_souls = item(name="Green lantern of eternal souls", description="A lantern containing the wandering souls before you.")
mimic_mage_scroll = item(name="Mimic Scroll The Power Of Magic", description="A magic scroll containing magic spells that a mage mimic might find handy.")