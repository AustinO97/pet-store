from models.__init__ import CURSOR, CONN
from models.pet_type import PetType

class PetStore:
    def __init__(self):
        self.pet_types = {}
        self.pets = []

    def add_pet_type(self, pet_type):
        self.pet_types[pet_type.name] = pet_type

    def add_pet(self, pet_name, pet):
        if pet_name in self.pet_types:
            self.pet_types[pet_name].add_pet(pet)
            self.pets.append(pet)
        else:
            print(f"Pet type '{pet_name}' does not exist in the store.")

    def list_available_pets(self):
        for pet_type in self.pet_types.values():
            print(pet_type)

    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY,
            name TEXT,
            species TEXT,
            breed TEXT,
            age INT
            )
        '''
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE IF EXISTS pets
        '''
        CURSOR.execute(sql)
        CONN.commit()