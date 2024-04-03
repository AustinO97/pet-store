from models.pet_store import PetStore
from models.pet import Pet

def reset_database():

    Pet.drop_table()
    PetStore.drop_table()
    
    Pet.create_table()
    PetStore.create_table()

reset_database()
petstore = PetStore.create('Petstore', 'Alton')
ryleigh = Pet.create('Ryleigh', 'cat', 'black/white', 3, 150, petstore.id)
lobster = Pet.create('Lobster', 'cat', 'orange', 2, 150, petstore.id)
bean = Pet.create('Bean', 'cat', 'spotted', 1, 0, None)