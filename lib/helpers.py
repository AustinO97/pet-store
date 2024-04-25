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
    store_name = input("Enter the pet's store : ")
    age_input = input("Enter the pet's age (press Enter if stray): ")
    age = int(age_input) if age_input else 'Unknown'
    price_input = input("Enter the pet's price (press Enter if stray): ")
    price = int(price_input) if price_input else 'Free'

    try:
        store = PetStore.find_by_name(store_name)
        store_id = store.id if store else None
        pet = Pet.create(name, species, breed, age, price, store_id)
        print(f'Pet {pet.name} added!') if pet else None
    except Exception as exc:
        print('Error creating pet: ', exc)

def display_pets():
    print('')
    pets = Pet.get_all()
    for pet in pets:
        idx = pets.index(pet) + 1
        print(f'{idx}. Name: {pet.name} | Species: {pet.species} | Breed: {pet.breed} | Age: {pet.age} | Price: {pet.price} | Store: {pet.store_id}')

def find_pet_by_breed():
    print('')
    pet_breed = input("Enter the pet's breed: ")
    pets = Pet.find_by_breed(pet_breed)
    if pets:
        print(f'Here are the pets that match the breed {pet_breed}:')
        for pet in pets:
            print(f'Name: {pet.name} | Species: {pet.species} | Breed: {pet.breed} | Age: {pet.age} | Price: {pet.price} | Store: {pet.store_id}')
    else:
        print('No pets found with that breed')

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
            store_name = input("Enter the pet's new store: ") or None
            if store_name:
                store = PetStore.find_by_name(store_name)
                if store:
                    pet.store_id = store.id
                else:
                    print("Store not found. Pet's store remains unchanged.")
            else:
                pet.store_id = None

            pet.update()
            print(f'Success: {pet.name} updated!')
        except Exception as exc:
            print('Error updating pet: ', exc)
    else:
        print(f'Pet {name} not found')

def delete_pet():
    print('')
    search_input = input("Enter the pet's name or ID: ")
    if search_input.isdigit():
        pet_id = int(search_input)
        if pet := Pet.find_by_id(pet_id):
            pet.delete()
            print(f'Pet with ID {pet_id} deleted')
        else:
            print(f'Pet with ID {pet_id} not found')
    else:
        if pet := Pet.find_by_name(search_input):
            pet.delete()
            print(f'Pet {search_input} deleted')
        else:
            print(f'Pet {search_input} not found')

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

def find_store_by_location():
    print('')
    store_location = input("Enter the stores location: ")
    stores = PetStore.find_by_location(store_location)
    if stores:
        print(f'Here are the stores that match the location {store_location}:')
        for store in stores:
            print(f'Name: {store.name} | {store.location}')
    else:
        print('No stores found with that location, store names are case sensitive')

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