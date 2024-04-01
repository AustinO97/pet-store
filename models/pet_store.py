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
            CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY,
            name TEXT,
            species TEXT,
            breed TEXT,
            age INT,
            price INT,
            store_id INT,
            FOREIGN KEY (store_id) REFERENCES store(id)
            )
        '''
        CURSOR.execute(sql)
        CONN.commit()