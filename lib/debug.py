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
petstore = PetStore.create('Petstore', 'Alton')
ryleigh = Pet.create('Ryleigh', 'cat', 'black/white', 3, 150, petstore.id)
lobster = Pet.create('Lobster', 'cat', 'orange', 2, 150, petstore.id)
bean = Pet.create('bean', 'cat', 'spotted', 1, 0, None)


ipdb.set_trace()
