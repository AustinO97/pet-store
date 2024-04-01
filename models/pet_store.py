from models.__init__ import CURSOR, CONN

class PetStore:

    all = {}

    def __init__(self, name, location, id = None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f'<Store {self.id}: {self.name}, {self.location}>'
    
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

        CURSOR.execute(sql, (self.name, self.location))
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

