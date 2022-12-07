
class item:
    def __init__(self, name, description = "This item doesn't have a description.", consumed = False):
        self.name = name
        self.description = description

class magic_orb(item):
    def __init__(self, colour, name, description):
        self.colour = colour
        self.name = name
        self.description = description

magic_orb = magic_orb(name="Magic Orb", description="Magic orb that can glow in multiple different colours such as yellow, red and blue.. Is also controlled by voice commands.", colour="Blue")
