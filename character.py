from random import randint

class Character():
    def __init__(self, gender: bool(), tattoos, inventory = dict(), name: str(), alive = True, level = 1):
        self.gender = c.MALE
        self.level = level
        if spells == None:
            self.spells = generate_character(level, c.DEFAULT_SPELLS)
        else:
            self.spells = spells
        if self.gender = None:
            self.generate_gender()
        if inventory == None:
            self.inventory = generate_default(level, c.DEFAULT_INVENTORY)
        self.name = name
        self.level = 1
        self.alive = True
        self.energy =
    def mortimus(self):
        if self.alive = False:
            
    def generate_gender(self):
        gender = randint(0,1)
        if gender == 0:
            self.gender = FEMALE
        else: 
            self.gender = MALE

def generate_default(level: int(), default: dict()) -> dict():
"""generates a default character attribute from character level"""
    try:
        level = int(level)
        if int(level) > 1 and int(level) < len(level):
            options = c.default
            default = options[level]
        else:
            Raise CustomError("character must be between %i and %i", 1, len(level))
    Except ValueError:
        Raise CustomError("character level must be a valid interger")

    return character_spells

def generate_default_name()
def generate_default_inventory(level)
    try:
        level = int(level)
        if int(level) > 1 and int(level) < len(level):
            options = c.DEFAULT_SPELLS
             = options[level]
        else:
            Raise CustomError("character must be between %i and %i", 1, len(level))
    Except ValueError:
        Raise CustomError("character level must be a valid interger")
    
    def create_name(self, new_name: str()):)
        if new_name.is_identifier(): 
            print("A name is the individuals most important trait, for it bestows the magician control over their very makeup; whether it be magical, physical, or devine. Your name must:")
            print("\n")
            print(format_bullet("A name must start with a letter or the underscore character.)"))
            print(format_bullet("A name cannot start with a number."))
            print(format_bullet("A name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )"))
            print(format_bullet("Names are case-sensitive (kathrine and Kathrine and KATHRINE are three different names)"))
        else:
            
            print("Nice to meet you %s, I believe your name is very fitting")