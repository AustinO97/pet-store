
from models.pet_type import PetType
from models.pet import Pet

class PetStore:
    def __init__(self):
        self.pet_types = {}
        self.pets = []

    # def add_pet_type(self, pet_type):
    #     sql = '''
    #         INSTERT INTO pet_types (name)
    #         VALUES (?)
    #     '''
    #     CURSOR.execute(sql, (self.name, ))

    # def add_pet(self, pet_name, pet):
    #     if pet_name in self.pet_types:
    #         self.pet_types[pet_name].add_pet(pet)
    #         self.pets.append(pet)
    #     else:
    #         print(f"Pet type '{pet_name}' does not exist in the store.")

    # def list_available_pets(self):
    #     for pet_type in self.pet_types.values():
    #         print(pet_type)

