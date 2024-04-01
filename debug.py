from models.__init__ import CONN, CURSOR
from models.pet_store import PetStore
from models.pet import Pet
import ipdb;

def reset_database():
    Pet.drop_table()
    Pet.create_table()

reset_database()

roo = Pet.create('roo', 'cat', 'black/white', 3, 150)
lobs = Pet.create('lobs', 'cat', 'orange', 2, 150)
bean = Pet.create('bean', 'cat', 'spotted', 1, 0)

ipdb.set_trace()
