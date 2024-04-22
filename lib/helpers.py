from models.pet_store import PetStore
from models.pet import Pet

def exit_program():
    print("Goodbye!")
    exit()

# Pet helper functions
    
def add_pet():
    print('')
    name = input("Enter the pet's name (enter Unknown if stray): ")
    species = input("Enter the pet's species : ")
    breed = input("Enter the pet's breed (enter Unknown if stray): ")
    store = input("Enter the pet's store (enter Unknown if stray): ")
    age_input = input("Enter the pet's age (press Enter if stray): ")
    age = int(age_input) if age_input else 'Unknown'
    price_input = input("Enter the pet's price (press Enter if stray): ")
    price = int(price_input) if price_input else 'Free'
    # age = input("Enter the pet's age: ")
    # price = input("Enter the pet's price: ")

    try:
        pet = Pet.create(name, species, breed, age, price, store)
        print(f'Pet {pet.name} added!') if pet else None
    except Exception as exc:
        print('Error creating pet: ', exc)

def display_pets():
    print('')
    pets = Pet.get_all()
    for pet in pets:
        idx = pets.index(pet) + 1
        print(f'{idx}. Name: {pet.name} | Species: {pet.species} | Breed: {pet.breed} | Age: {pet.age} | Store: {pet.store_name}')

def update_pet():
    print('')
    name = input("Enter the pet's name: ")
    if pet := Pet.find_by_name(name):
        try:
            name = input("Enter the pet's new name: ") or pet.name
            pet.name = name
            breed = input("Enter the pet's breed: ") or pet.breed
            pet.breed = breed
            age_input = input("Enter the pet's age : ")
            age = int(age_input) if age_input else pet.age
            pet.age = age
            price_input = input("Enter the pet's price : ")
            price = int(price_input) if price_input else pet.price
            pet.price = price
            store = input("Enter the pet's new store: ") or pet.store_name
            pet.store = store

            pet.update()
            print(f'Success: {pet.name} updated!')
        except Exception as exc:
            print('Error updating pet: ', exc)
    else:
        print(f'Pet {name} not found')

def delete_pet():
    print('')
    name = input("Enter the pet's name: ")
    if pet := Pet.find_by_name(name):
        pet.delete()
        print(f'Pet {name} deleted')
    else:
        print(f'Pet {name} not found')

# PetStore helper functions
        
def add_pet_store():
    print('')
    name = input("Enter the new pet store name: ")
    location = input("Enter the new pet store locaton: ")

    try:
        store = PetStore.create(name, location)
        print(f'Store {store.name} added!') if store else None
    except Exception as exc:
        print('Error creating store: ', exc)

def display_pet_stores():
    print('')
    stores = PetStore.get_all()
    for store in stores:
        idx = stores.index(store) + 1
        print(f'{idx}. Store Name: {store.name} | Location: {store.location}')

def update_pet_store():
    print('')
    name = input("Enter the store's name: ")
    if store := PetStore.find_by_name(name):
        try:
            name = input("Enter the store's new name: ") or store.name
            store.name = name
            location = input("Enter the store's new location: ") or store.location
            store.location = location

            store.update()
            print(f'Success: {store.name} updated!')
        except Exception as exc:
            print('Error updating store: ', exc)
    else:
        print(f'Store {name} not found')

def delete_pet_store():
    print('')
    name = input("Enter the store's name: ")
    if store := PetStore.find_by_name(name):
        store.delete()
        print(f'Store {name} deleted')
    else:
        print(f'Store {name} not found')