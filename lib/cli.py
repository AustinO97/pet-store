from helpers import (
    add_pet, 
    display_pets, 
    find_pet_by_breed, 
    update_pet, 
    delete_pet, 
    add_pet_store, 
    display_pet_stores, 
    find_store_by_location, 
    update_pet_store, 
    delete_pet_store
)

class Main:

    def display_main_menu(self):
        print('\nPet Management System')
        print('1. Manage Pets')
        print('2. Manage Pet Stores')
        print('3. Quit')

    def display_pet_menu(self):
        print('\nPet Management Menu')
        print('1. Add a Pet')
        print('2. View All Pets')
        print('3. View Pets by breed')
        print('4. Update a Pet')
        print('5. Delete a Pet')
        print('6. Back to Main Menu')

    def display_store_menu(self):
        print('\nPet Store Management Menu')
        print('1. Add a Pet Store')
        print('2. View All Pet Stores')
        print('3. View Stores by location')
        print('3. Update a Pet Store')
        print('4. Delete a Pet Store')
        print('5. Back to Main Menu')


    def run(self):
        while True:
            self.display_main_menu()
            choice = input('Enter your choice: ')
            if choice == '1':
                self.pet_management()
            elif choice == '2':
                self.store_management()
            elif choice == '3':
                print('Exiting program...')
                break
            else:
                print('Invalid choice. Please try again.')

    def pet_management(self):
        while True:
            self.display_pet_menu()
            choice = input('Enter your choice: ')
            if choice == '1':
                add_pet()
            elif choice == '2':
                display_pets()
            elif choice == '3':
                find_pet_by_breed()
            elif choice == '4':
                update_pet()
            elif choice == '5':
                delete_pet()
            elif choice == '6':
                break
            else:
                print('Invalid choice. Please try again.')

    def store_management(self):
        while True:
            self.display_store_menu()
            choice = input('Enter your choice: ')
            if choice == '1':
                add_pet_store()
            elif choice == '2':
                display_pet_stores()
            elif choice == '3':
                find_store_by_location()
            elif choice == '4':
                update_pet_store()
            elif choice == '5':
                delete_pet_store()
            elif choice == '6':
                break
            else:
                print('Invalid choice. Please try again')



if __name__ == "__main__":
    cli = Main()
    cli.run()