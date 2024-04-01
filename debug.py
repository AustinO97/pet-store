from models.__init__ import CONN, CURSOR
from models.pet_store import PetStore
from models.pet import Pet
import ipdb;

def reset_database():
    Pet.drop_table()
    Pet.create_table()

reset_database()


ipdb.set_trace()
