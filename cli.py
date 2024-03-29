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
            pet = input('Enter the name of the pet >>>')
            species = input('Enter the species of the pet >>>')
            breed = input('Enter the breed of the pet >>>')
            age = input('Enter the age of the pet >>>')
            pet_list.append([pet, species, breed, age])
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