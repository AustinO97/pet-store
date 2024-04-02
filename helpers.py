from models.pet_store import PetStore
from models.pet import Pet

def exit_program():
    print("Goodbye!")
    exit()

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
        print('')
        print('Error creating pet: ', exc)

def display_pet_list():
    print('')
    pets = Pet.get_all()
    for pet in pets:
        print(pet)