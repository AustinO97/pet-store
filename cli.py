from models.pet import Pet
from models.pet_store import PetStore

class Main():

    def display_main_menu(self):
        print('\nPet Management System')
        print('1. Manage Pets')
        print('2. Manage Pet Stores')
        print('3. Quit')

    def display_pet_management_menu(self):
        print('\nPet Management Menu')
        print('1. Add a Pet')
        print('2. View All Pets')
        print('3. Update a Pet')
        print('4. Delete a Pet')
        print('5. Back to Main Menu')

    def display_store_management_menu(self):
        print('\nPet Store Management Menu')
        print('1. Add a Pet Store')
        print('2. View All Pet Stores')
        print('3. Update a Pet Store')
        print('4. Delete a Pet Store')
        print('5. Back to Main Menu')


    def run(self):
        while True:
            self.display_main_menu()
            choice = input('Enter your choice: ')
            if choice == '1':
                self.run_pet_management()
            elif choice == '2':
                self.run_store_management()
            elif choice == '3':
                print('Exiting program...')
                break
            else:
                print('Invalid choice. Please try again.')



if __name__ == "__main__":
    pass