from models.__init__ import CURSOR, CONN
class Pet:

    all = {}

    def __init__(self, name, species, breed, age, price, store_name, id = None):
        self.id = id
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.price = price
        self.store_name = store_name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise Exception('Name must be a string with 3 or more characters')
        
    @property
    def species(self):
        return self._species
    
    @species.setter
    def species(self, species):
        if isinstance(species, str) and len(species):
            self._species = species
        else:
            raise Exception('Species must be a non-empty string')
        
    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, breed):
        if isinstance(breed, str) and len(breed):
            self._breed = breed
        else:
            raise Exception('Breed must be a non-empty string')
          
    # @property
    # def price(self):
    #     return self._price
    
    # @price.setter
    # def price(self, price):
    #     if isinstance(price, int):
    #         self._price = price
    #     else:
    #         raise Exception('Price must be an integer')

    # @property
    # def age(self):
    #     return self._age
    
    # @age.setter
    # def age(self, age):
    #     if isinstance(age, int):
    #         self._age = age
    #     else:
    #         raise Exception('Age must be an integer')

    @property
    def store_name(self):
        return self._store_name
    
    @store_name.setter
    def store_name(self, store_name):
        if isinstance(store_name, str) and len(store_name) >= 3:
            self._store_name = store_name
        else:
            raise Exception('Store name must be a string with 3 or more characters')

    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY,
            name TEXT,
            species TEXT,
            breed TEXT,
            age INT,
            price INT,
            store_name TEXT,
            FOREIGN KEY (store_name) REFERENCES stores(name)
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
            INSERT INTO pets (name, species, breed, age, price, store_name)
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        CURSOR.execute(sql, (self.name, self.species, 
                             self.breed, self.age, 
                             self.price, self.store_name))
        CONN.commit()

        self.id = CURSOR.lastrowid

        Pet.all[self.id] = self

    @classmethod
    def create(cls, name, species, breed, age, price, store_name):
        pet = cls(name, species, breed, age, price, store_name)
        pet.save()
        return pet
    
    def update(self):
        sql = '''
            UPDATE pets
            SET name = ?, species = ?, breed = ?, age = ?, price = ?, store_name = ?
            WHERE id = ?
        '''

        CURSOR.execute(sql, (self.name, self.species, 
                             self.breed, self.age, self.price, 
                             self.store_name, self.id))
        CONN.commit()

    def delete(self):
        sql = '''
            DELETE FROM pets
            WHERE id = ?
        '''

        CURSOR.execute(sql, (self.id, ))
        CONN.commit()

        del Pet.all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        pet = cls.all.get(row[0])
        if pet:
            pet.name = row[1]
            pet.species = row[2]
            pet.breed = row[3]
            pet.age = row[4]
            pet.price = row[5]
            pet.store_name = row[6]
        else:
            pet = cls(row[1], row[2], row[3], row[4], row[5], row[6])
            pet.id = row[0]
            cls.all[pet.id] = pet
        return pet
    
    @classmethod
    def get_all(cls):
        sql = '''
            SELECT * FROM pets
        '''

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_name(cls, name):
        sql = '''
            SELECT *
            FROM pets
            WHERE name = ?
        '''

        row = CURSOR.execute(sql, (name, )).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def store(self):
        from models.pet_store import PetStore
        sql = '''
            SELECT * FROM stores
            WHERE name = ?
        '''

        row = CURSOR.execute(sql, (self.store_name, )).fetchone()
        store = PetStore.instance_from_db(row)
        return store
    
    # def __repr__(self):
    #     return f'<Pet {self.id}: {self.name}'