from models.pet_store import PetStore
from models.pet import Pet


Pet.drop_table()
PetStore.drop_table()

Pet.create_table()
PetStore.create_table()

petstore = PetStore.create('Petstore', 'Alton')
ryleigh = Pet.create('Ryleigh', 'cat', 'black/white', 3, 150, petstore.id)
lobster = Pet.create('Lobster', 'cat', 'orange', 2, 150, petstore.id)
bean = Pet.create('Bean', 'cat', 'spotted', 1, 0, None)
dobby = Pet.create('Dobby', 'dog', 'doberman pinscher', 1, 0, None)