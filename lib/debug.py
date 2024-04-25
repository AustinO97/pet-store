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
furyfriends = PetStore.create('Fury Friends', 'Jupiter')
ryleigh = Pet.create('Ryleigh', 'cat', 'domestic short hair', 3, 150, furyfriends.id)
lobster = Pet.create('Lobster', 'cat', 'orange tabby', 2, 150, petsmart.id)
bean = Pet.create('Bean', 'cat', 'black tabby', 1, 'Free', None)
dobby = Pet.create('Dobby', 'dog', 'doberman pinscher mix', 1, 'Free', None)
pat = Pet.create('Pat', 'dog', 'golden retriever', 2, 200, petsmart.id)


ipdb.set_trace()
