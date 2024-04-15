Pet-Store

ABOUT Pet Store is a CLI application that allows you to manage pets and manage stores. Users can add, view, update and delete pets / stores.

HOW TO USE THE APPLICATION 
Run pipenv install to create your virtual environment and pipenv shell to enter the virtual environment.

Type in 'python lib/cli.py' to start the main menu.

Pet Management System
1. Manage Pets
2. Manage Pet Stores
3. Quit
Enter your choice:

Users can enter the manage pets menu by pressing 1 and perform the following tasks:
1. Add a Pet
2. View All Pets
3. Update a Pet
4. Delete a Pet
5. Back to Main Manu
Users can enter the manage stores menu by pressing 2 and perform the following tasks:
1. Add a Pet Store
2. View All Pet Stores
3. Update a Pet Store
4. Delete a Pet Store
5. Back to Main Menu

The directory structure is as follows:

.
└── lib
    ├── models
        ├── __init__.py
        ├── pet_store.py
        └── pet.py
    ├── cli.py
    ├── debug.py
    ├── helpers.py
    └── seed.py
├── Pipfile
├── Pipfile.lock
├── README.md
├── store.db

Seeding the database with sample data
The file lib/seed.py contains code to initialize the database with sample departments and employees. Run the following command to seed the database:

python lib/seed.py
You can use the SQLITE EXPLORER extension to explore the initial database contents. (Another alternative is to run python lib/debug.py and use the ipbd session to explore the database)