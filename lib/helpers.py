from models.pet_store import PetStore
from models.pet import Pet

def exit_program():
    print("Goodbye!")
    exit()

# Pet helper functions
    
def add_pet():
    print('')
    name = input("Enter the pet's name: ")
    species = input("Enter the pet's species: ")
    breed = input("Enter the pet's breed: ")
    age = input("Enter the pet's age: ")
    price = input("Enter the pet's price: ")
    store_id = input("Enter the pet's store: ")
    try:
        pet = Pet.create(name, species, breed, age, price, store_id)
        print(pet) if pet else None
    except Exception as exc:
        print('Error creating pet: ', exc)

def display_pet_list():
    print('')
    pets = Pet.get_all()
    for pet in pets:
        print(pet)

def update_pet():
    print('')
    id_ = input("Enter the pet's id: ")
    if pet := Pet.find_by_id(id_):
        try:
            name = input("Enter the pet's new name: ")
            pet.name = name
            price = input("Enter the pet's new price: ")
            pet.price = price
            store_id = input("Enter the pet's new store: ")
            pet.store_id = store_id

            pet.update()
            print(f'Success: {pet}')
        except Exception as exc:
            print('Error updating pet: ', exc)
    else:
        print(f'Pet {id_} not found')

def delete_pet():
    print('')
    id_ = input("Enter the pet's id: ")
    if pet := Pet.find_by_id(id_):
        pet.delete()
        print(f'Pet {id_} deleted')
    else:
        print(f'Pet {id_} not found')

# PetStore helper functions
        
def add_pet_store():
    print('')
    name = input("Enter the new pet store name: ")
    location = input("Enter the new pet store locaton: ")

    try:
        store = PetStore.create(name, location)
        print(store) if store else None
    except Exception as exc:
        print('Error creating store: ', exc)