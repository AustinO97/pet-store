from models.__init__ import CURSOR, CONN

class Pet_store:
    def __init__(self, name, species, breed, age):
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.pets = []

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
            DROP TABLE IF EXITS pets
        '''
        CURSOR.execute(sql)
        CONN.commit()

    def add_pet(self, pet):
        self.pets.append(pet)