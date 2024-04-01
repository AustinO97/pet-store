from models.__init__ import CURSOR, CONN
class Pet:

    all = {}

    def __init__(self, name, species, breed, age, price, id = None):
        self.id = id
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.price = price

    def __repr__(self):
        return f'<Pet {self.id}: {self.name}, {self.breed}, {self.age}, {self.price}>'

    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY,
            name TEXT,
            species TEXT,
            breed TEXT,
            age INT,
            price INT
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

    def save(self):
        sql = '''
            INSERT INTO pets (name, species, breed, age, price)
            VALUES (?, ?, ?, ?, ?)
        '''
        CURSOR.execute(sql, (self.name, self.species, self.breed, self.age, self.price))
        CONN.commit()

        self.id = CURSOR.lastrowid

        Pet.all[self.id] = self

    @classmethod
    def create(cls, name, species, breed, age, price):
        pet = cls(name, species, breed, age, price)
        pet.save()
        return pet
    
    def update(self):
        sql = '''
            UPDATE pets
            SET name = ?, species = ?, breed = ?, age = ?, price = ?
            WHERE id = ?
        '''

        CURSOR.execute(sql, (self.name, self.species, self.breed, self.age, self.price, self.id))
        CONN.commit()

    def delete(self):
        sql = '''
            DELETE FROM pets
            WHERE id = ?
        '''

        CURSOR.execute(sql, (self.id, ))
        CONN.commit()

