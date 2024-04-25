from models.__init__ import CURSOR, CONN

class PetStore:

    all = {}

    def __init__(self, name, location, id = None):
        self.id = id
        self.name = name
        self.location = location
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 3:
            self._name = name
        else:
            raise Exception('Name must be a string with more than 3 characters')
        
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, location):
        if isinstance(location, str) and len(location) > 3:
            self._location = location
        else:
            raise Exception('Location must be a string with more than 3 characters')
    
    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS stores (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT
            )
        '''
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE IF EXISTS stores
        '''

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = '''
            INSERT INTO stores (name, location)
            VALUES (?, ?)
        '''

        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()

        self.id = CURSOR.lastrowid

        PetStore.all[self.id] = self

    @classmethod
    def create(cls, name, location):
        store = cls(name, location)
        store.save()
        return store
    
    def update(self):
        sql = '''
            UPDATE stores
            SET name = ?, location = ?
            WHERE id = ?
        '''

        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        sql = '''
            DELETE FROM stores
            WHERE id = ?
        '''

        CURSOR.execute(sql, (self.id, ))
        CONN.commit()

        del PetStore.all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        store = cls.all.get(row[0])
        if store:
            store.name = row[1]
            store.location = row[2]
        else:
            store = cls(row[1], row[2])
            store.id = row[0]
            cls.all[store.id] = store
        return store
    
    @classmethod
    def get_all(cls):
        sql = '''
            SELECT * FROM stores
        '''

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_name(cls, name):
        sql = '''
            SELECT * 
            FROM stores
            WHERE name = ?
        '''

        row = CURSOR.execute(sql, (name, )).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def pets(self):
        from models.pet import Pet
        sql = '''
            SELECT * FROM pets
            WHERE store_id = ?
        '''

        rows = CURSOR.execute(sql, (self.id, )).fetchall()

        return [Pet.instance_from_db(row) for row in rows]
    
    def __repr__(self):
        return f'<Pet Store {self.id}: {self.name}'