from models.__init__ import CONN, CURSOR
from models.pet_store import PetStore
from models.pet import Pet
import ipdb;

def reset_database():
    Pet.drop_table()
    Pet.create_table()
    PetStore.drop_table()
    PetStore.create_table()

reset_database()
petsmart = PetStore.create('Petsmart', 'Alton')
roo = Pet.create('roo', 'cat', 'black/white', 3, 150, petsmart.id)
lobs = Pet.create('lobs', 'cat', 'orange', 2, 150, petsmart.id)
bean = Pet.create('bean', 'cat', 'spotted', 1, 0, petsmart.id)


ipdb.set_trace()
