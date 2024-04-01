from models.pet import Pet
from models.pet_store import PetStore
from models.pet_type import PetType

def main():
    pet_list = []

    choice = 0
    while True:
        print('*** pet Manager ***')
        print('1) Add a pet')
        print('2) Lookup a pet')
        print('3) Display pets')
        print('4) Quit')
        choice = int(input())

        if choice == 1:
            print('Adding a pet...')
            name = input('Enter the name of the pet >>>')
            species = input('Enter the species of the pet >>>')
            breed = input('Enter the breed of the pet >>>')
            price = input('Enter the price of the pet >>>')
            new_pet = Pet(name, species, breed, price)
            pet_list.append(new_pet)
        elif choice == 2:
            print('Looking up a pet...')
            keyword = input('Enter Search Term: ')
            for pet in pet_list:
                if keyword in pet:
                    print(pet)
        elif choice == 3:
            print('Displaying all pets...')
            for i in range(len(pet_list)):
                print(pet_list[i])
        elif choice == 4:
            print('Quitting program')
            exit()



if __name__ == "__main__":
    main()