class PetType:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def __repr__(self):
        return f"{self.name} Pets: {', '.join(p.name for p in self.pets)}"