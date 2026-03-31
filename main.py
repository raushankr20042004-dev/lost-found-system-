from manager import add_lost_item, add_found_item, find_matches

def menu():
    while True:
        print("\n1. Report Lost Item")
        print("2. Report Found Item")
        print("3. Find Matches")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Item name: ")
            desc = input("Description: ")
            add_lost_item(name, desc)

        elif choice == '2':
            name = input("Item name: ")
            desc = input("Description: ")
            add_found_item(name, desc)

        elif choice == '3':
            find_matches()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice")

menu()
