from models.__init__ import CURSOR, CONN

class PetStore:
    def __init__(self, name, location, id = None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f'<Store {self.id}: {self.name}, {self.location}>'
    
    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS store (
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
            DELETE TABLE IF EXISTS store
        '''

        CURSOR.execute(sql)
        CONN.commit()