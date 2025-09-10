def add(key, value, dict1):
    dict1[key] = value

def remove(key, dict1):
    if key in dict1:
        del dict1[key]
        print(f"{key} removed.")
    else:
        print("Key not found.")

def search(key, dict1):
    if key in dict1:
        print(f"{key} -> {dict1[key]}")
    else:
        print("Key not found.")

def update(key, newvalue, dict1):
    if key in dict1:
        dict1[key] = newvalue
        print(f"{key} updated to {newvalue}.")
    else:
        print("Key not found.")

def display(dict1):
    print("Current Dictionary:")
    for k, v in dict1.items():
        print(f"{k}: {v}")

def totalcount(dict1):
    print('Total number of books:', len(dict1))

def searchonvalue(value, dict1):
    found = False
    for k, v in dict1.items():
        if v == value:
            print(f"{k} -> {v}")
            found = True
    if not found:
        print("Value not found.")


dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


while True:
    print("\nMENU:")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search a book by key")
    print("4. Update a book")
    print("5. Display all books")
    print("6. Total count of books")
    print("7. Search book(s) by value")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        k = input("Enter book key: ")
        v = int(input("Enter book value: "))
        add(k, v, dict1)
    elif choice == '2':
        k = input("Enter book key to remove: ")
        remove(k, dict1)
    elif choice == '3':
        k = input("Enter book key to search: ")
        search(k, dict1)
    elif choice == '4':
        k = input("Enter book key to update: ")
        v = int(input("Enter new value: "))
        update(k, v, dict1)
    elif choice == '5':
        display(dict1)
    elif choice == '6':
        totalcount(dict1)
    elif choice == '7':
        v = int(input("Enter value to search: "))
        searchonvalue(v, dict1)
    elif choice == '8':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
