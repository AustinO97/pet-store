def main():
    cat_list = []

    choice = 0
    while choice != 4:
        print('*** Cat Manager ***')
        print('1) Add a cat')
        print('2) Lookup a cat')
        print('3) Display cats')
        print('4) Quit')
        choice = int(input())

        if choice == 1:
            print('Adding a cat...')
            cat = input('Enter the name of the cat >>>')
            owner = input('Enter the name of the owner >>>')
            breed = input('Enter the breed of the cat >>>')
            age = input('Enter the age of the cat >>>')
            cat_list.append([cat, owner, breed, age])
        elif choice == 2:
            print('Looking up a cat...')
            keyword = input('Enter Search Term: ')
            for cat in cat_list:
                if keyword in cat:
                    print(cat)
        elif choice == 3:
            print('Displaying all cats...')
            for i in range(len(cat_list)):
                print(cat_list[i])
        elif choice == 4:
            print('Quitting program')



if __name__ == "__main__":
    main()